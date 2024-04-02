from marshmallow import EXCLUDE, fields

from app.schemas.base import BaseSchema


class ProductCheckoutSchema(BaseSchema):
    name = fields.Str()
    support_button = fields.Bool()
    counter = fields.Bool()
    color = fields.Bool()
    notifications = fields.Bool()
    ask_email = fields.Bool()
    is_exclusive = fields.Bool()
    product_id = fields.Int()

    class Meta:
        unknown = EXCLUDE
        exclude = ('created_at', 'updated_at')
