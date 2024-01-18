from marshmallow import EXCLUDE, fields

from app.schemas.base import BaseSchema
from app.services import spec


class GroupSchema(BaseSchema):
    name = fields.Str(required=True)
    status = fields.Boolean()

    class Meta:
        unknown = EXCLUDE
        exclude = ('created_at', 'updated_at')
