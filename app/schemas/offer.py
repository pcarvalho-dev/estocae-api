from marshmallow import EXCLUDE, fields

from app.schemas.base import BaseSchema


class OfferSchema(BaseSchema):
    name = fields.Str(required=True)
    url = fields.Str()
    price = fields.Float(required=True)
    custom_commission = fields.Float()
    quantity = fields.Int()
    status = fields.Str()
    product_id = fields.Int()

    class Meta:
        unknown = EXCLUDE
        exclude = ('created_at', 'updated_at')
