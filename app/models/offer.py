from app import db
from app.models.base import BaseModel


class Offer(db.Model, BaseModel):
    __tablename__ = "offer"

    name = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255))
    price = db.Column(db.Float, nullable=False)
    custom_commission = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    status = db.Column(db.String(255), default="active")
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))

    coupon = db.relationship("Coupon", back_populates="offer")

    def __init__(self, **kwargs):
        allowed_args = self.__mapper__.class_manager  # returns a dict
        kwargs = {k: v for k, v in kwargs.items() if k in allowed_args}
        super().__init__(**kwargs)
