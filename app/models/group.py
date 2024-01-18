from app import db
from app.models.base import BaseModel


# It creates a table called group with the columns name and status.
class Group(db.Model, BaseModel):
    __tablename__ = 'group'

    name = db.Column(db.String(255))
    status = db.Column(db.Boolean(), nullable=False, default=1)
