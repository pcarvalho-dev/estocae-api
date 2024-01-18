from app import models, schemas
from app.controllers import CRUDBase
from app.services.errors.exceptions import ConflictError


class CrudTermsAndConditions(CRUDBase):

    def update_terms_and_conditions(self, item_id, schema):
        extra_filters = [('id', 'eq', item_id)]
        item = self.get_first(extra_filters=extra_filters)

        if item.status == 'PUBLISHED':
            raise ConflictError(
                "Updating is not allowed because the term has already been published")

        item = self.put(item_id=item_id, schema=schema)

        return item

    def delete_terms_and_conditions(self, item_id):
        self.delete(item_id=item_id)

    def publish_terms_and_conditions(self, item_id):
        extra_filters = [('id', 'eq', item_id)]
        item = self.get_first(extra_filters=extra_filters)

        if item.status == 'PUBLISHED':
            raise ConflictError(
                "Updating is not allowed because the term has already been published")

        item.status = 'PUBLISHED'
        item.update()

        item_return = self.class_schema().dump(item)

        return item_return


crud_terms_and_conditions = CrudTermsAndConditions(models.TermsAndConditions,
                                                   schemas.TermsAndConditionsSchema)
