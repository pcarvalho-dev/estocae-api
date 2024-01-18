from flask import request

from app import models, schemas
from app.controllers import CRUDBase
from app.controllers.terms_and_conditions import crud_terms_and_conditions


class CrudUserTermsAndConditions(CRUDBase):

    def agree_terms_and_conditions(self, user_id, user_group):
        documents_type = ['PRIVACY_POLICY', 'TERMS_OF_USE']
        if user_group == 4:
            documents_type = ['PRIVACY_POLICY', 'TERMS_OF_USE',
                              "HOST_AGREEMENT", "TERMS_OF_USE_HOSTS"]

        dict_body = request.get_json()
        if not user_id:
            user_id = dict_body['user_id']

        for document_type in documents_type:
            extra_filters = [('document_type', 'eq', document_type),
                             ('status', 'eq', 'PUBLISHED')]
            term = crud_terms_and_conditions.get_last(extra_filters=extra_filters,
                                                      active_order=True, order='id',
                                                      order_by='desc')

            if term:
                term_filter = [('terms_and_conditions_id', 'eq', term.id),
                               ('user_id', 'eq', user_id)]
                term_agree = self.get_first(extra_filters=term_filter)

                if term_agree is None:
                    payload = dict(user_id=user_id, status='AGREE',
                                   terms_and_conditions_id=term.id)
                    self.post(dict_body=payload, is_dict=True)
        msg = 'Successfully accepted terms and conditions'
        return msg

    @staticmethod
    def list_terms_and_conditions_to_agree():
        document_type = request.args.get('document_type')
        extra_filters = [('document_type', 'eq', document_type),
                         ('status', 'eq', 'PUBLISHED')]

        item = crud_terms_and_conditions.get_last(extra_filters=extra_filters,
                                                  active_order=True, order='id',
                                                  order_by='desc', schema=True)

        return item


crud_user_terms_and_conditions = CrudUserTermsAndConditions(
    models.UserTermsAndConditions,
    schemas.UserTermsAndConditionsSchema)
