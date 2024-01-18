from marshmallow import EXCLUDE, fields

from app.schemas.base import BaseSchema
from app.services import spec


class CitySchema(BaseSchema):
    name = fields.Str(required=True)
    status = fields.Boolean()

    state_id = fields.Int(required=True, load_only=True)
    state = fields.Nested('StateSchema',
                          exclude=('created_at', 'updated_at'), dump_only=True)

    class Meta:
        unknown = EXCLUDE
        exclude = ('created_at', 'updated_at')
