from marshmallow import EXCLUDE, fields

from app.schemas.base import BaseSchema


class ProductAffiliateSchema(BaseSchema):
    user_id = fields.Int()
    product_id = fields.Int()

    class Meta:
        unknown = EXCLUDE
        exclude = ('created_at', 'updated_at')
