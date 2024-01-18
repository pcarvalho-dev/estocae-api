from marshmallow import EXCLUDE, fields

from app.schemas.base import BaseSchema


class MainSettingsSchema(BaseSchema):
    logo_image_key = fields.Str()

    primary_color = fields.Str(required=True)
    second_color = fields.Str(required=True)
    third_color = fields.Str()
    fourth_color = fields.Str()
    fifth_color = fields.Str()
    sixth_color = fields.Str()

    primary_text_color = fields.Str()
    second_text_color = fields.Str()
    third_text_color = fields.Str()
    fourth_text_color = fields.Str()
    fifth_text_color = fields.Str()
    sixth_text_color = fields.Str()

    class Meta:
        unknown = EXCLUDE
        exclude = ('created_at', 'updated_at')
