import os
import uuid

from flask import request

from app import models, schemas
from app.controllers import CRUDBase, crud_user_address
from app.controllers.user_validators import UserValidators
from app.services.errors.exceptions import UnauthorizedError, \
    ConflictError
from app.services.security.password import get_password_hash, verify_password


class CRUDUser(CRUDBase):

    @staticmethod
    def create_and_update_address(user_id, dict_address):

        extra_filters = [('user_id', 'eq', user_id)]
        address = crud_user_address.get_first(extra_filters)
        if address:
            crud_user_address.put(item_id=address.id,
                                  dict_body=dict_address)
        else:
            extra_fields = [('user_id', user_id)]
            crud_user_address.post(dict_body=dict_address,
                                   extra_fields=extra_fields)

    def create_user(self, schema, specific_group_id=False):
        """
        It creates a user and validates the payment
        
        :param specific_group_id: Set specific user id
        :param validate_if_exist: Validate identification document
        :param schema: The schema to use for validation
        :return: The return is a string, but I need to return the item.
        """
        dict_body = request.get_json()

        # verify exist

        UserValidators(dict_body=dict_body,
                       type_request="POST",
                       item_id=None).active_all()

        # add hash_id and hash in password
        extra_fields = [("hash_id", str(uuid.uuid4())),
                        ("password", get_password_hash(dict_body['password']))]

        # specific group id
        if specific_group_id:
            extra_fields.append(("group_id", specific_group_id))

        dict_address = None
        if 'address' in dict_body:
            dict_address = dict_body.pop('address')

        item = self.post(extra_fields=extra_fields, dict_body=dict_body)

        if dict_address:
            extra_fields = [("user_id", item.id)]
            crud_user_address.post(dict_body=dict_address,
                                   extra_fields=extra_fields)

        if schema:
            item = self.class_schema().dump(item)

        return item

    def update_user(self, schema, item_id):
        dict_body = request.get_json()
        UserValidators(dict_body=dict_body,
                       type_request="PUT",
                       item_id=item_id).active_all()

        dict_address = dict_body.pop('address')

        item = self.put(item_id=item_id, schema=False, dict_body=dict_body)

        if dict_address:
            self.create_and_update_address(item_id, dict_address)

        if 'password' in dict_body:
            item.set_password(password=dict_body['password'])

        item.update()

        if schema:
            item = self.class_schema().dump(item)

        return item

    def get_user_by_jwt(self, user_jwt, schema=None):
        """
        It returns the first user that matches the hash_id in the user_jwt, has a status of 1, and has a
        deleted_at of None

        :param user_jwt: The JWT token that is passed in the header
        :return: A user object
        """
        item = self.class_model.query.filter(
            self.class_model.hash_id == user_jwt['hash_id'],
            self.class_model.status.is_(True),
            self.class_model.deleted_at.is_(None)).first()

        if schema:
            item = self.class_schema().dump(item)

        return item

    def validate_auth_request(self, username, basic):
        query = self.class_model.query.filter(
            self.class_model.status.is_(True),
            self.class_model.deleted_at.is_(None))

        if basic != os.environ.get("ADMIN_BASIC"):
            raise UnauthorizedError("Invalid Basic Negado Header")

        if "@" in username:
            query = query.filter(self.class_model.email == username)
        else:
            query = query.filter(self.class_model.cpf == username)

        user = query.first()

        return user

    def update_password(self, item_id, schema=None):
        dict_body = request.get_json()
        user = self.get(item_id)

        if user is not None and verify_password(user.password,
                                                dict_body['password']):

            password = get_password_hash(dict_body['new_password'])
            user.password = password
            user.update()

        else:
            raise ConflictError("Senha antiga incorreta!")

        if schema:
            user = self.class_schema().dump(user)

        return user


# Creating an instance of the class CRUDUser.
crud_user = CRUDUser(models.User, schemas.UserSchema)
