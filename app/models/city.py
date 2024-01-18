from app import db
from app.models.state import State
from app.models.base import BaseModel


# The City class has a one-to-many relationship with the State class
class City(db.Model, BaseModel):
    __tablename__ = 'city'

    name = db.Column(db.String(255))
    status = db.Column(db.Boolean(), nullable=False, default=1)

    # foreign key
    state_id = db.Column(db.Integer, db.ForeignKey('state.id'))

    # relationship
    state = db.relationship(State, uselist=False, backref="city")
