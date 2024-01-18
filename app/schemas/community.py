from marshmallow import EXCLUDE, fields

from app.schemas.base import BaseSchema
from app.services import spec


class CommunitySchema(BaseSchema):
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    is_active = fields.Boolean()
    auto_approved_user = fields.Boolean()

    user_id = fields.Int(load_only=True)

    user = fields.Nested('UserSchema', exclude=('created_at', 'updated_at'),
                         dump_only=True)

    class Meta:
        unknown = EXCLUDE
        exclude = ('created_at', 'updated_at')
