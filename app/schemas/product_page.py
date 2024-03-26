from marshmallow import EXCLUDE, fields

from app.schemas.base import BaseSchema


class ProductPageSchema(BaseSchema):
    name = fields.Str()
    link = fields.Str()
    product_id = fields.Int()

    class Meta:
        unknown = EXCLUDE
        exclude = ('created_at', 'updated_at')
