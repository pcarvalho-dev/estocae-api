from marshmallow import EXCLUDE, fields

from app.schemas.base import BaseSchema
from app.services import spec


class CountrySchema(BaseSchema):
    name_global = fields.Str(required=True)
    name = fields.Str(required=True)
    code = fields.Str(required=True)
    code_alpha2 = fields.Str(required=True)
    code_alpha3 = fields.Str(required=True)
    status = fields.Boolean()

    class Meta:
        unknown = EXCLUDE
        exclude = ('created_at', 'updated_at')
