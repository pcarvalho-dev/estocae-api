from marshmallow import EXCLUDE, fields

from app.schemas.base import BaseSchema


class MainCompanySchema(BaseSchema):
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    cell_phone = fields.Str(required=True)
    landline = fields.Str(required=True)
    status = fields.Boolean()

    ein = fields.Str(required=True)
    company_name = fields.Str(required=True)

    facebook = fields.Str()
    instagram = fields.Str()
    app_android = fields.Str()
    app_ios = fields.Str()

    address = fields.Nested('MainCompanyAddressSchema',
                            exclude=('created_at', 'updated_at'),
                            dump_only=True)

    class Meta:
        unknown = EXCLUDE
        exclude = ('created_at', 'updated_at')
