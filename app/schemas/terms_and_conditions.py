from marshmallow import fields, validate

from app.schemas.base import BaseSchema


class TermsAndConditionsSchema(BaseSchema):
    title = fields.Str()
    status = fields.Str(dump_only=True,
                        validate=validate.OneOf(["AWAITING_PUBLICATION", "PUBLISHED"]))
    content = fields.Str()
    document_type = fields.Str(required=True,
                               validate=validate.OneOf([
                                   "PRIVACY_POLICY",
                                   "TERMS_OF_USE",
                                   "HOST_AGREEMENT",
                                   "TERMS_OF_USE_HOSTS",
                               ]))

    class Meta:
        ordered = True
