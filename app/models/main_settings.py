from app import db
from app.models.base import BaseModel


class MainSettings(db.Model, BaseModel):
    __tablename__ = "main_settings"

    logo_image_key = db.Column(db.String(255))

    primary_color = db.Column(db.String(255))
    second_color = db.Column(db.String(255))
    third_color = db.Column(db.String(255))
    fourth_color = db.Column(db.String(255))
    fifth_color = db.Column(db.String(255))
    sixth_color = db.Column(db.String(255))

    primary_text_color = db.Column(db.String(255))
    second_text_color = db.Column(db.String(255))
    third_text_color = db.Column(db.String(255))
    fourth_text_color = db.Column(db.String(255))
    fifth_text_color = db.Column(db.String(255))
    sixth_text_color = db.Column(db.String(255))

    main_company_id = db.Column(db.Integer, db.ForeignKey("main_company.id"))
