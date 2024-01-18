from marshmallow import Schema, fields


class ImageSchema(Schema):
    original = fields.Str(dump_only=True)
    small = fields.Str(dump_only=True)
    medium = fields.Str(dump_only=True)
    large = fields.Str(dump_only=True)

    class Meta:
        ordered = True


class BaseSchema(Schema):
    id = fields.Int(dump_only=True)
    hash_id = fields.Str(dump_only=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

    class Meta:
        ordered = True
