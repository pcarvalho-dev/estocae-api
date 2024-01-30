from app import db
from app.models.base import BaseModel
from sqlalchemy.dialects.mysql import LONGTEXT


class Product(db.Model, BaseModel):
    __tablename__ = "product"

    name = db.Column(db.String(255), nullable=False)
    description = db.Column(LONGTEXT(collation="utf8mb4_bin"))
    sales_link = db.Column(db.String(255))
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(255), default="active")

    def __init__(self, **kwargs):
        allowed_args = self.__mapper__.class_manager  # returns a dict
        kwargs = {k: v for k, v in kwargs.items() if k in allowed_args}
        super().__init__(**kwargs)
