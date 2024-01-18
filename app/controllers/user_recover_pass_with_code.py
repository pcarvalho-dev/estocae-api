import random
import uuid
import datetime

from app.controllers import crud_user_code_password
from app.controllers.send_email import SendEmail

from app.controllers.user import crud_user
from app.services.errors.exceptions import BadRequestError
from app.services.security.password import get_password_hash


class RecoverPassWithCode:
    def __init__(self, username=None):
        self.username = username

    def recover(self):
        if '@' in self.username:
            extra_filters = [("email", "eq", self.username)]
            msg = f'O email: {self.username}, não possui registro na nossa base'
        else:
            extra_filters = [("cellphone", "eq", self.username)]
            msg = f'O celular: {self.username}, não possui registro na nossa base'

        item = crud_user.get_first(extra_filters=extra_filters)

        if item is None:
            raise BadRequestError(message=msg)

        # update token
        item.token_update = str(uuid.uuid4())
        item.update()

        extra_filters = [("email", "eq", item.email)]
        code = crud_user_code_password.get_first(extra_filters=extra_filters)
        if code:
            code.deleted_at = datetime.datetime.now()
            item.update()

        payload = {
            "email": item.email,
            "validation_date": datetime.datetime.now() + datetime.timedelta(
                minutes=3),
            "code": random.randint(10000, 99998)
        }

        new_code = crud_user_code_password.post(schema=True,
                                                dict_body=payload,
                                                is_dict=True)

        SendEmail(item.name, item.email).reset_pass(new_code['code'])

        return item.email

    @staticmethod
    def validate_code(dict_body):
        extra_filters = [("email", "eq", dict_body['email']),
                         ("code", "eq", dict_body['code'])]
        item = crud_user_code_password.get_first(extra_filters=extra_filters)

        if item is None:
            raise BadRequestError(message=f'Invalid code')

        now = datetime.datetime.now()
        code_time = item.validation_date
        time_expiration = (code_time - now).seconds

        if time_expiration > 180:
            raise BadRequestError(message=f'Expired validation code')

        item.deleted_at = datetime.datetime.now()
        item.update()

        extra_filters = [("email", "eq", dict_body['email'])]
        user = crud_user.get_first(extra_filters=extra_filters)

        payload = {
            "token_update": user.token_update
        }
        return payload

    @staticmethod
    def reset_pass(dict_body):
        extra_filters = [("email", "eq", dict_body['email']),
                         ("token_update", "eq", dict_body["token_update"])]
        item = crud_user.get_first(extra_filters=extra_filters)

        if item is None:
            raise BadRequestError(
                message=f'User not found or Token not validate')
        password = get_password_hash(dict_body['password'])

        item.token_update = str(uuid.uuid1())
        item.password = password
        item.update()
