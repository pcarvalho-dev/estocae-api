from marshmallow import Schema, fields
from app.schemas.base import BaseSchema


class UserCodePassword(BaseSchema):
    email = fields.Email()
    validation_date = fields.DateTime()
    code = fields.Integer()

    class Meta:
        ordered = True


class CheckCode(UserCodePassword):
    class Meta:
        ordered = True
        exclude = ('validation_date',)


class ReturnEmail(Schema):
    email = fields.Email()


class ReturnTokenUpdate(Schema):
    token_update = fields.Str()
