from marshmallow import fields, validate

from app.schemas.base import BaseSchema


class UserTermsAndConditionsSchema(BaseSchema):
    user_id = fields.Int(load_only=True)
    terms_and_conditions_id = fields.Int(load_only=True)
    status = fields.Str(dump_only=True, validate=validate.OneOf(["AGREE"]))

    class Meta:
        ordered = True
