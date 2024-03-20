from app import db
from app.models.base import BaseModel


class Coupon(db.Model, BaseModel):
    __tablename__ = "coupon"

    name = db.Column(db.String(255), nullable=False)
    discount_percent = db.Column(db.Float, nullable=False)
    limit = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(255), default="active")

    offer_id = db.Column(db.Integer, db.ForeignKey("offer.id"))
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))
    offer = db.relationship("Offer", back_populates="coupon")

    def __init__(self, **kwargs):
        allowed_args = self.__mapper__.class_manager  # returns a dict
        kwargs = {k: v for k, v in kwargs.items() if k in allowed_args}
        super().__init__(**kwargs)
