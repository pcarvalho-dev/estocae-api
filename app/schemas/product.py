from marshmallow import EXCLUDE, fields

from app.schemas.base import BaseSchema


class ProductSchema(BaseSchema):
    name = fields.Str(required=True)
    description = fields.Str()
    sales_link = fields.Str()
    price = fields.Float(required=True)
    comission_percent = fields.Int()
    warranty_period = fields.Int()
    weight = fields.Float()
    packing_type = fields.Str()
    status = fields.Str()

    class Meta:
        unknown = EXCLUDE
        exclude = ('created_at', 'updated_at')
