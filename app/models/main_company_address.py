from app import db
from app.models.base import BaseModel
from app.models.city import City


class MainCompanyAddress(db.Model, BaseModel):
    __tablename__ = "main_company_address"

    code_post = db.Column(db.String(256))
    street = db.Column(db.String(256))
    number = db.Column(db.String(256))
    district = db.Column(db.String(256))
    complement = db.Column(db.String(256))

    lat = db.Column(db.String(256))
    long = db.Column(db.String(256))

    city_id = db.Column(db.Integer, db.ForeignKey("city.id"))
    main_company_id = db.Column(db.Integer, db.ForeignKey("main_company.id"))

    city = db.relationship(City, uselist=False, backref="company_address")
