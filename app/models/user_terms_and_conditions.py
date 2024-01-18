from app import db
from app.models.base import BaseModel


class UserTermsAndConditions(db.Model, BaseModel):
    __tablename__ = 'user_terms_and_conditions'

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    terms_and_conditions_id = db.Column(db.Integer, db.ForeignKey('terms_and_conditions.id'))
    status = db.Column(db.String(255))

