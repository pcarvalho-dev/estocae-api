from app import db
from app.models.base import BaseModel


class ProductPage(db.Model, BaseModel):
    __tablename__ = "product_page"

    name = db.Column(db.String(255), nullable=False)
    link = db.Column(db.String(255), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))

    def __init__(self, **kwargs):
        allowed_args = self.__mapper__.class_manager  # returns a dict
        kwargs = {k: v for k, v in kwargs.items() if k in allowed_args}
        super().__init__(**kwargs)
