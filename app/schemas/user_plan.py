from marshmallow import EXCLUDE, fields

from app.schemas.base import BaseSchema


class UserPlanSchema(BaseSchema):
    user_id = fields.Integer()
    plan_id = fields.Integer()
    status = fields.String()

    class Meta:
        unknown = EXCLUDE
        exclude = ('created_at', 'updated_at')
