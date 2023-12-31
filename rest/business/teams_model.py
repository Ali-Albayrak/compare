import os
import importlib

from actions import create_player_for_team


import enum
from sqlalchemy import DATETIME, String, ForeignKey
from sqlalchemy import String, ForeignKey, Column, Text
from sqlalchemy.orm import relationship
from core.base_model import BaseModel
from core.manager import Manager

class CustomManager(Manager):

    def post_save(self, **kwargs) -> dict:
        jwt = kwargs.get("jwt", {})
        new_data = kwargs.get("new_data", {})
        old_data = kwargs.get("old_data", {})
        well_known_urls = kwargs.get("well_known_urls", {})
        new_data = create_player_for_team.handler(jwt=jwt, new_data=new_data, old_data=old_data, well_known_urls=well_known_urls, method="create")
        return new_data






# select enums


class TeamModel(BaseModel):
    __tablename__ = 'teams'
    __table_args__ = {'schema': os.environ.get('DEFAULT_SCHEMA', 'public')}

            
    name = Column(Text, nullable=False, default=None)
            
    location = Column(Text, nullable=True, default=None)
            
    short_name = Column(Text, nullable=True, default=None)
            
    bio = Column(Text, nullable=True, default=None)
    
    
    owner = Column(String, ForeignKey("public.users.id"))

         
    players = relationship('PlayerModel', back_populates='team__details')
    
    @classmethod
    def objects(cls, session):
        return CustomManager(cls, session)
