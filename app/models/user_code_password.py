from app import db
from app.models.base import BaseModel


class UserCodePassword(db.Model, BaseModel):
    _tablename_ = 'user_code_password'

    email = db.Column(db.String(255))
    validation_date = db.Column(db.DateTime)
    code = db.Column(db.Integer)
