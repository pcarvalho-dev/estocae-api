from marshmallow import fields

from app.schemas.base import BaseSchema


class MainCompanyAddressSchema(BaseSchema):
    code_post = fields.Str(required=True)
    street = fields.Str(required=True)
    number = fields.Str()
    district = fields.Str(required=True)
    complement = fields.Str()
    city_id = fields.Int(required=True, load_only=True)

    city = fields.Nested('CitySchema', exclude=('created_at', 'updated_at'),
                         dump_only=True)

    class Meta:
        ordered = True

