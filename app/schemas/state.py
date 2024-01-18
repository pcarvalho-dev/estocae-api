from marshmallow import EXCLUDE, fields

from app.schemas.base import BaseSchema
from app.services import spec


class StateSchema(BaseSchema):
    name = fields.Str(required=True)
    uf = fields.Str(required=True)
    status = fields.Boolean()

    country_id = fields.Int(required=True, load_only=True)

    country = fields.Nested('CountrySchema',
                            exclude=('created_at', 'updated_at'), dump_only=True)

    class Meta:
        unknown = EXCLUDE
        exclude = ('created_at', 'updated_at')
