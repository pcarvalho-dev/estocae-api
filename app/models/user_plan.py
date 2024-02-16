from app import db
from app.models.base import BaseModel


class UserPlan(db.Model, BaseModel):
    _tablename_ = 'user_plan'

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))
    status = db.Column(db.String(255), default='pending')
