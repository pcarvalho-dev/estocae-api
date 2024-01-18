from app import db
from app.models.base import BaseModel


# The UserAddress class has a one-to-one relationship with the User class and a one-to-one
# relationship with the City class
class UserAddress(db.Model, BaseModel):
    __tablename__ = "user_address"

    code_post = db.Column(db.String(256))
    street = db.Column(db.String(256))
    number = db.Column(db.String(256))
    district = db.Column(db.String(256))
    complement = db.Column(db.String(256))

    lat = db.Column(db.String(256))
    long = db.Column(db.String(256))

    # foreign key
    city_id = db.Column(db.Integer, db.ForeignKey("city.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    # relationship
    city = db.relationship('City', uselist=False, backref="user_address")
