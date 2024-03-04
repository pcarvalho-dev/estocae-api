from marshmallow import EXCLUDE, fields

from app.schemas.base import BaseSchema


class PlanSchema(BaseSchema):
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    description = fields.Str()
    status = fields.Str()
    comission_percent = fields.Float()
    group = fields.Nested('GroupSchema', dump_only=True)

    class Meta:
        unknown = EXCLUDE
        exclude = ('created_at', 'updated_at')
