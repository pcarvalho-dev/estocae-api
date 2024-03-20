from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request
from sqlalchemy.dialects.mysql import LONGTEXT

from app import db, models
from app.models.base import BaseModel


class Product(db.Model, BaseModel):
    __tablename__ = "product"

    name = db.Column(db.String(255), nullable=False)
    description = db.Column(LONGTEXT(collation="utf8mb4_bin"))
    sales_link = db.Column(db.String(255))
    price = db.Column(db.Float, nullable=False)
    warranty_period = db.Column(db.Integer)
    weight = db.Column(db.Float)
    packing_type = db.Column(db.String(255))
    status = db.Column(db.String(255), default="active")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # Affiliation
    is_affiliation = db.Column(db.Boolean, default=False)
    is_visible_in_store = db.Column(db.Boolean, default=True)
    affiliation_name = db.Column(db.String(255))
    cookie_time = db.Column(db.Integer)
    affiliation_type = db.Column(db.String(255))

    def _get_comission_percent(self):
        try:
            verify_jwt_in_request()
            user_jwt = get_jwt_identity()
            user = models.User.get_by_id(user_jwt['user_id'])
            return user.comission_percent
        except:
            return 10
    comission_percent = property(_get_comission_percent)

    def __init__(self, **kwargs):
        allowed_args = self.__mapper__.class_manager  # returns a dict
        kwargs = {k: v for k, v in kwargs.items() if k in allowed_args}
        super().__init__(**kwargs)
