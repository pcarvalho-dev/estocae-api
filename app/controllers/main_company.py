from flask import request

from app import models, schemas
from app.controllers import CRUDBase, crud_main_company_address


class MainCompany(CRUDBase):

    def update_company(self, schema):
        dict_body = request.get_json()
        dict_adddress = dict_body.pop('address')

        item = self.put_first(dict_body=dict_body, is_dict=True)

        if dict_adddress:
            extra_filters = [('main_company_id', 'eq', item.id)]
            address = crud_main_company_address.get_first(
                extra_filters=extra_filters)
            if address:
                crud_main_company_address.put(
                    item_id=address.id,
                    is_dict=True,
                    dict_body=dict_adddress
                )
            else:
                extra_fields = [('main_company_id', item.id)]
                crud_main_company_address.post(
                    dict_body=dict_adddress,
                    is_dict=True,
                    extra_fields=extra_fields
                )

        if schema:
            item = self.class_schema().dump(item)

        return item


crud_main_company = MainCompany(models.MainCompany, schemas.MainCompanySchema)
