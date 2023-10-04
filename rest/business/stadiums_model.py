import os




import enum
from sqlalchemy import DATETIME, String, ForeignKey
from sqlalchemy import Integer, Enum, Column, Text
from sqlalchemy.orm import relationship
from core.base_model import BaseModel
from core.manager import Manager



# select enums
class TypeEnum(str, enum.Enum):
    covered = "covered"
    open = "open"


class StadiumModel(BaseModel):
    __tablename__ = 'stadiums'
    __table_args__ = {'schema': os.environ.get('DEFAULT_SCHEMA', 'public')}

            
    name = Column(Text, nullable=True, default=None)
            
    location = Column(Text, nullable=True, default=None)
            
    type = Column(Enum(TypeEnum), nullable=True, default=None)
            
    capacity = Column(Integer, nullable=True, default=None)

    @classmethod
    def objects(cls, session):
        return Manager(cls, session)
