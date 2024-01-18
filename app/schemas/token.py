from marshmallow import EXCLUDE, Schema, fields


class TokenSchema(Schema):
    username = fields.Str(required=True, load_only=True)
    password = fields.Str(required=True, load_only=True)
    grant_type = fields.Str(required=True, load_only=True)

    token_type = fields.Str(required=True, dump_only=True)
    expires_in = fields.Str(required=True, dump_only=True)
    access_token = fields.Str(required=True, dump_only=True)
    refresh_token = fields.Str(required=True, dump_only=True)

    class Meta:
        unknown = EXCLUDE
