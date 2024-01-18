import uuid
from datetime import datetime
from flask_sqlalchemy import Model
from sqlalchemy import Column, Integer, DateTime, String


# This class is a base class for all models in the application. It provides the basic fields and
# methods that all models need

class BaseModel(Model):
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    hash_id = Column(String(36), nullable=False,
                     default=lambda x: str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(),
                        onupdate=datetime.now())
    deleted_at = Column(DateTime)

    @classmethod
    def get_by_id(cls, record_id):
        """
        It takes a class and a record id, and returns the record with that id
        
        :param cls: The class that the method is being called on
        :param record_id: The id of the record you want to get
        :return: The query is being returned.
        """
        return cls.query.get(int(record_id))
