from app import db
from app.models.base import BaseModel


# The State class is a subclass of db.Model and BaseModel. It has a name, uf, status, and country_id
# column. It also has a country relationship
class State(db.Model, BaseModel):
    __tablename__ = 'state'

    name = db.Column(db.String(255))
    uf = db.Column(db.String(2), nullable=False)
    status = db.Column(db.Boolean(), nullable=False, default=1)

    # foreign key
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))

    # relationship
    country = db.relationship('Country', uselist=False, backref="state")
