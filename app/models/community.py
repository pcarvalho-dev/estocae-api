from app import db
from app.models.base import BaseModel


# The Community class is a model that represents a community. 
# It has a name, description, is_active, auto_approved_user, user_id, and user. 
# The user_id is a foreign key that references the id of the user who created the community. 
# The user is a relationship that references the user who created the community. 
# The user is a one-to-one relationship because the community can only have one user. 
# The user is a backref because the user can have many communities. 
# The user is lazy because the user is not loaded until it is needed. 
# The user is not a list because the community can only have one user. 
# The user is not a dynamic loader because the user is not loaded until it is needed.
class Community(db.Model, BaseModel):
    __tablename__ = 'community'

    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean(), nullable=False, default=1)
    auto_approved_user = db.Column(db.Boolean(), nullable=False, default=1)

    # foreign key
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    # relationship
    user = db.relationship('User', backref='community', lazy=True,
                           uselist=False)
