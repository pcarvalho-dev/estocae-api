from sqlalchemy.dialects.mysql import LONGTEXT

from app import db
from app.models.base import BaseModel


class Plan(db.Model, BaseModel):
    __tablename__ = "plan"

    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(LONGTEXT(collation="utf8mb4_bin"))
    status = db.Column(db.String(255), default="active")
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    comission_percent = db.Column(db.Float, default=0)
    group = db.relationship('Group', backref='plans')

    def __init__(self, **kwargs):
        allowed_args = self.__mapper__.class_manager  # returns a dict
        kwargs = {k: v for k, v in kwargs.items() if k in allowed_args}
        super().__init__(**kwargs)
