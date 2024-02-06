from app import db

from app.models.base import BaseModel

"""
Credential levels

1 - System / Sistema (desenvolvedores)
2 - Admin
3 - Editor
4 - Autor
5 - Client
"""


class User(db.Model, BaseModel):
    __tablename__ = "user"

    token_update = db.Column(db.String(36))
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    email_verified = db.Column(db.Boolean, default=0)
    cellphone = db.Column(db.String(255))
    document = db.Column(db.String(255))
    password = db.Column(db.String(255), nullable=False)
    image_key = db.Column(db.String(255))
    genre = db.Column(db.String(255))
    birth_date = db.Column(db.Date)
    comission_percent = db.Column(db.Integer)
    status = db.Column(db.Boolean(), nullable=False, default=1)

    # foreign key
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"))

    # relationship
    group = db.relationship('Group', backref='user', lazy=True, uselist=False)

    # address
    address = db.relationship('UserAddress', backref='user', lazy=True,
                                uselist=False)

    def __init__(self, **kwargs):
        allowed_args = self.__mapper__.class_manager  # returns a dict
        kwargs = {k: v for k, v in kwargs.items() if k in allowed_args}
        super().__init__(**kwargs)
