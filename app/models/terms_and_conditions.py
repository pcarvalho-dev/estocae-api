from sqlalchemy.dialects.mysql import LONGTEXT

from app import db
from app.models.base import BaseModel


class TermsAndConditions(db.Model, BaseModel):
    __tablename__ = 'terms_and_conditions'

    title = db.Column(db.String(255))
    content = db.Column(LONGTEXT(collation="utf8mb4_bin"))
    status = db.Column(db.String(255), default='AWAITING_PUBLICATION')
    document_type = db.Column(db.String(255))
