
from flask import request

from app import models, schemas
from app.controllers import CRUDBase


class CrudProduct(CRUDBase):
    
    def update_product(self, item_id):
        dict_body = request.get_json()

        item = self.put(item_id, dict_body=dict_body, is_dict=True)

        item = self.class_schema().dump(item)

        return item


# Creating an instance of the class CRUDUser.
crud_product = CrudProduct(models.Product, schemas.ProductSchema)
