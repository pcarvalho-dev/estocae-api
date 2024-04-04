from app.controllers import crud_city
from app.services.errors.exceptions import ConflictError


class UserValidators:

    def __init__(self, dict_body, type_request, item_id):
        from app.controllers.user import crud_user
        self.class_model = crud_user
        self.dict_body = dict_body
        self.type_request = type_request
        self.item_id = item_id

    def __query_validate_email(self, email):
        extra_filters = [("email", "eq", email)]
        item = self.class_model.get_first(extra_filters=extra_filters)

        if item:
            raise ConflictError(
                f'Já existe um usuário cadastrado com o email: {email} ')

    def __query_validate_city(self, city_id):
        extra_filters = [("id", "eq", city_id)]
        item = crud_city.get_first(extra_filters=extra_filters)

        if not item:
            raise ConflictError(
                f'Não existe cidade com este id: {city_id} ')

    def __query_validate_doc_value(self, taxpayer):

        if taxpayer is not None:
            if taxpayer != "":

                extra_filters = [("document", "eq", taxpayer)]
                item = self.class_model.get_first(extra_filters=extra_filters)

                if item:
                    raise ConflictError(
                        f'Já existe um usuário cadastrado com o cpf: {taxpayer} ')

    def __query_validate_cellphone(self, cellphone):
        extra_filters = [("cellphone", "eq", cellphone)]
        item = self.class_model.get_first(extra_filters=extra_filters)

        if item:
            raise ConflictError(
                f'Já existe um usuário cadastrado com o nº de celular: {cellphone} ')

    def validate_email(self):

        if self.type_request == 'PUT':
            item = self.class_model.get(item_id=self.item_id)
            if item.email != self.dict_body['email']:
                self.__query_validate_email(self.dict_body['email'])

        elif self.type_request == 'POST':
            self.__query_validate_email(self.dict_body['email'])

    def validate_doc_user(self):
        if self.type_request == 'PUT':
            item = self.class_model.get(item_id=self.item_id)
            if item.taxpayer != self.dict_body['document']:
                self.__query_validate_doc_value(self.dict_body['document'])

        elif self.type_request == 'POST':
            self.__query_validate_doc_value(self.dict_body['document'])

    def validate_cellphone(self):
        if self.type_request == 'PUT':
            item = self.class_model.get(item_id=self.item_id)
            if item.cellphone != self.dict_body['cellphone']:
                self.__query_validate_cellphone(self.dict_body['cellphone'])

        elif self.type_request == 'POST':
            self.__query_validate_cellphone(self.dict_body['cellphone'])

    def validate_city(self):
        self.__query_validate_city(self.dict_body['address']['city_id'])

    def active_all(self):
        self.validate_doc_user()
        self.validate_email()
        self.validate_cellphone()
        if "address" in self.dict_body:
            self.validate_city()

    def verify_user_admin(self):
        self.validate_email()
        self.validate_cellphone()
