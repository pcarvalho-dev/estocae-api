import uuid

from flask import request
from marshmallow import ValidationError
from sqlalchemy import or_, func

from app.services.aws.s3 import delete_file_s3, get_aws_image_keys_private, \
    upload_image_s3_by_item, upload_file_s3, get_aws_file
from app.services.errors.exceptions import GenerateError, NotFoundError
from app.services.requests.params import custom_parameters
from app.services.sqlalchemy.dynamic_filters import dynamic_filters


class CRUDBase:
    def __init__(self, class_model, class_schema, class_schema_create=None,
                 class_schema_update=None):
        """
        A constructor function that initializes the class.
        
        :param class_model: The model class that will be used to query the database
        :param class_schema: This is the schema that will be used for GET requests
        :param class_schema_create: The schema to use when creating a new object
        :param class_schema_update: The schema to use for updating an existing object
        """

        if class_schema_create is None:
            class_schema_create = class_schema

        if class_schema_update is None:
            class_schema_update = class_schema

        self.class_model = class_model
        self.class_schema = class_schema
        self.class_schema_create = class_schema_create
        self.class_schema_update = class_schema_update

    def post(self, schema=None, extra_fields=None, dict_body=None,
             is_dict=None):
        """
        It takes a dictionary, validates it against a schema, and then creates a new object in the database
        
        :param schema: The schema to use to serialize the object
        :param extra_fields: a list of tuples that will be added to the dict_body
        :param dict_body: The dictionary that will be validated
        :param is_dict: If True, the data will be validated as a dict. If False, it will be validated as a
        list
        :return: A dictionary with the following keys:
        """

        if dict_body is None:
            dict_body = request.get_json()

        if extra_fields:
            for field in extra_fields:
                key, value = field
                dict_body[key] = value

        try:
            if is_dict:
                self.class_schema_create().from_dict(dict_body)
            else:
                self.class_schema_create().load(dict_body)
        except ValidationError as error:
            raise GenerateError(status_code=400, error='Bad Request',
                                errors=error.messages)

        item = self.class_model.create(**dict_body)

        if schema:
            item = self.class_schema().dump(item)
        return item

    def get(self, item_id, schema=None, columns=None):
        """
        It takes an item_id, and returns the item with that id, if it exists
        
        :param item_id: The id of the item to be retrieved
        :param schema: The schema to use to serialize the object
        :param columns: ['id', 'name', 'description']
        :return: {
            "id": 1,
            "name": "test",
            "deleted_at": null
        }
        """
        query = self.class_model.query.filter(
            self.class_model.deleted_at.is_(None))
        if columns:
            query = query.with_entities(
                *[getattr(self.class_model, column) for column in columns])
        item = query.filter(self.class_model.id == item_id).first()
        if not item:
            raise NotFoundError()
        if schema:
            item = self.class_schema().dump(item)
        return item

    def get_first(self, extra_filters=None, schema=None, columns=None):
        """
        It takes a model, a query, and a dictionary of filters, and returns a query with the filters applied
        
        :param extra_filters: a dictionary of filters to be applied to the query
        :param schema: The schema to use to serialize the data
        :param columns: list of columns to return
        :return: A list of dictionaries
        """
        query = self.class_model.query.filter(
            self.class_model.deleted_at.is_(None))
        if columns:
            query = query.with_entities(
                *[getattr(self.class_model, column) for column in columns])

        if extra_filters:
            query = dynamic_filters(self.class_model, query, extra_filters)

        item = query.first()

        if schema:
            if item:
                item = self.class_schema().dump(item)
        return item

    def get_multi(self, schema=None, columns=None, extra_filters=None,
                  active_order=None):
        """
        It gets the data from the database, filters it, paginates it, and returns it
        
        :param schema: The schema to be used to serialize the data
        :param columns: list of columns to be returned
        :param extra_filters: {'id': 1}
        :param active_order: Boolean
        :return: A tuple with two elements.
        """

        page, per_page, search, order, order_by = custom_parameters()

        query = self.class_model.query.filter(
            self.class_model.deleted_at.is_(None))

        if columns:
            query = query.with_entities(
                *[getattr(self.class_model, column) for column in columns])

        if search:
            query = query.filter(
                or_(self.class_model.name.like(f'%%{search}%%')))

        if extra_filters:
            query = dynamic_filters(self.class_model, query, extra_filters)

        if active_order:
            column_sorted = getattr(getattr(self.class_model, order),
                                    order_by)()
            query = query.order_by(column_sorted)

        items = query.paginate(page, per_page, False)
        items_paginate = items

        if schema:
            items = self.class_schema(many=True).dump(items.items)

        return items, items_paginate

    def get_count_total(self, search=None, extra_filters=None):
        """
        It returns the total number of rows in the table, but only if the row has not been deleted
        
        :param search: is a string that is used to search for a specific record
        :param extra_filters: {'name': 'test'}
        :return: A query object
        """
        query = self.class_model.query.filter(
            self.class_model.deleted_at.is_(None))

        query = query.with_entities(func.count())

        if search:
            query = query.filter(
                or_(self.class_model.name.like(f'%%{search}%%')))

        if extra_filters:
            query = dynamic_filters(self.class_model, query, extra_filters)

        query = query.scalar()

        return query

    def put(self, item_id, schema=None, dict_body=None, is_dict=None):
        """
        It updates the item in the database.
        
        :param item_id: the id of the item to be updated
        :param schema: The schema to use for validation
        :param dict_body: The dictionary that is passed in from the request
        :param is_dict: True if the dict_body is a dictionary, False if it's a JSON string
        """
        item = self.get(item_id)

        if dict_body is None:
            dict_body = request.get_json()

        try:
            if is_dict:
                self.class_schema_update().from_dict(dict_body)
            else:
                self.class_schema_update().load(dict_body)
        except ValidationError as error:
            raise GenerateError(status_code=400, error='Bad Request',
                                errors=error.messages)

        item.update(**dict_body)
        if schema:
            item = self.class_schema().dump(item)
        return item

    def put_first(self, schema=None, dict_body=None, is_dict=None):
        """
        It updates the item in the database.

        :param item_id: the id of the item to be updated
        :param schema: The schema to use for validation
        :param dict_body: The dictionary that is passed in from the request
        :param is_dict: True if the dict_body is a dictionary, False if it's a JSON string
        """
        item = self.get_first()

        if dict_body is None:
            dict_body = request.get_json()

        try:
            if is_dict:
                self.class_schema_update().from_dict(dict_body)
            else:
                self.class_schema_update().load(dict_body)
        except ValidationError as error:
            raise GenerateError(status_code=400, error='Bad Request',
                                errors=error.messages)

        item.update(**dict_body)
        if schema:
            item = self.class_schema().dump(item)
        return item

    def delete(self, item_id, delete_real=None):
        """
        It deletes an item from the database and deletes the associated image and file from S3
        
        :param item_id: The id of the item to delete
        :return: True
        """
        item = self.get(item_id)

        try:
            if item.image_key is not None:
                delete_file_s3(item.image_key)
        except:
            pass

        try:
            if item.file_key is not None:
                delete_file_s3(item.file_key)
        except:
            pass

        if delete_real:
            item.delete_real()
        else:
            item.delete()

        return True

    def put_image(self, id, slug):
        """
        It takes an id and a slug, gets the item from the database, deletes the old image from S3, uploads
        the new image to S3, updates the database with the new image key, and returns the new image key
        
        :param id: the id of the item
        :param slug: the name of the image
        :return: The data is being returned from the put_image function.
        """
        item = self.get(id)
        # delete old
        if item.image_key is not None:
            delete_file_s3(item.image_key)

        # upload new aws
        upload = upload_image_s3_by_item(item, slug)

        # update new db
        item.image_key = upload["image_key"]
        item.update()

        data = get_aws_image_keys_private(upload["image_key"])

        return data

    def delete_image(self, id):
        """
        It deletes an image from AWS S3 and updates the database
        
        :param id: the id of the item
        :return: The return value is a boolean value.
        """
        item = self.get(id)

        # delete image from aws
        delete_file_s3(item.image_key)

        # update db
        item.image_key = None
        item.update()

        return True

    def put_file(self, item_id, column_key, path, specific_image=None):
        """
        It takes an id and a slug, gets the item from the database, deletes the old image from S3, uploads
        the new image to S3, updates the database with the new image key, and returns the new image key

        :param item_id: the id of the item
        :param column_key: the name of the image
        :param path: the name of the path
        :return: The data is being returned from the put_image function.
        """
        item = self.get(item_id)
        # delete old
        key_file_aws = getattr(item, column_key)

        if key_file_aws is not None:
            delete_file_s3(key_file_aws)

        hash_code = str(uuid.uuid1())
        # upload new aws
        upload, type_data = upload_file_s3(hash_code=hash_code, path=path,
                                           specific_image=specific_image)

        # update new db
        setattr(item, column_key, upload["file_key"])
        item.update()

        data = get_aws_file(upload["file_key"], type_data=type_data)

        return data

    def delete_file(self, item_id, column_key):
        """
        It deletes an image from AWS S3 and updates the database
        :param item_id: the id of the item
        :param column_key: the name of the column key aws
        :return: The return value is a boolean value.
        """
        item = self.get(item_id)
        file_key_aws = getattr(item, column_key)

        if file_key_aws is None:
            raise NotFoundError(
                message='Não existe o arquivo para ser deletado')

        # delete image from aws
        delete_file_s3(file_key_aws)

        # update db
        setattr(item, column_key, None)
        item.update()

        return True
