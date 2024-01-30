from marshmallow import EXCLUDE, fields

from app.schemas.base import BaseSchema


class UserSchema(BaseSchema):
    hash_id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    cellphone = fields.Str()
    document = fields.Str()
    password = fields.Str(required=True, load_only=True)
    genre = fields.Str()
    birth_date = fields.Date()
    status = fields.Boolean()

    group_id = fields.Int(required=True)

    group = fields.Nested('GroupSchema',
                          exclude=('created_at', 'updated_at'), dump_only=True)
    address = fields.Nested('UserAddressSchema', many=False,
                            exclude=('created_at', 'updated_at'))

    class Meta:
        unknown = EXCLUDE
        exclude = ('created_at', 'updated_at')
