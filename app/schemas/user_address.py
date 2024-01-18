from marshmallow import EXCLUDE, fields

from app.schemas.base import BaseSchema


class UserAddressSchema(BaseSchema):
    code_post = fields.Str(required=True)
    street = fields.Str(required=True)
    number = fields.Str()
    district = fields.Str()
    complement = fields.Str()

    user_id = fields.Int(required=True)
    city_id = fields.Int(required=True, load_only=True)

    city = fields.Nested('CitySchema', exclude=(
        'created_at', 'updated_at'), dump_only=True)

    class Meta:
        unknown = EXCLUDE
        exclude = ('created_at', 'updated_at')
