from app import db
from app.models.base import BaseModel


# It creates a table called country in the database.
class Country(db.Model, BaseModel):
    __tablename__ = 'country'

    name_global = db.Column(db.String(255))
    name = db.Column(db.String(255), nullable=False)
    code = db.Column(db.String(255), nullable=False)
    code_alpha2 = db.Column(db.String(2), nullable=False)
    code_alpha3 = db.Column(db.String(3))
    status = db.Column(db.Boolean(), nullable=False, default=1)
