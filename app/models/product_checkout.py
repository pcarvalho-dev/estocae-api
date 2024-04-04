from app import db
from app.models.base import BaseModel


class ProductCheckout(db.Model, BaseModel):
    __tablename__ = "product_checkout"
    name = db.Column(db.String(255), nullable=False)
    support_button = db.Column(db.Boolean, nullable=False)
    counter = db.Column(db.Boolean, nullable=False)
    color = db.Column(db.Boolean, nullable=False)
    notifications = db.Column(db.Boolean, nullable=False)
    ask_email = db.Column(db.Boolean, nullable=False)
    is_exclusive = db.Column(db.Boolean, nullable=False)

    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))

    def __init__(self, **kwargs):
        allowed_args = self.__mapper__.class_manager  # returns a dict
        kwargs = {k: v for k, v in kwargs.items() if k in allowed_args}
        super().__init__(**kwargs)
