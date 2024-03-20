from marshmallow import EXCLUDE, fields

from app.schemas.base import BaseSchema


class CouponSchema(BaseSchema):
    name = fields.Str(required=True)
    discount_percent = fields.Float(required=True)
    limit = fields.Int()
    status = fields.Str()

    offer_id = fields.Int()
    product_id = fields.Int()
    offer = fields.Nested('OfferSchema', exclude=('created_at', 'updated_at'))

    class Meta:
        unknown = EXCLUDE
        exclude = ('created_at', 'updated_at')
