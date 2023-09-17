from sqlalchemy import Column, VARCHAR, BIGINT, TEXT, INTEGER
from .base import BaseModel


class User(BaseModel):
    __tablename__ = 'users'
    
    user_id = Column(BIGINT, unique=True, nullable=False, primary_key=True)
    
    username = Column(VARCHAR(32), unique=False, nullable=True)
    
class Horo(BaseModel):
    __tablename__ = 'horo'
    
    zodiac = Column(VARCHAR(32), unique=True, primary_key=True)
    
    horo_today = Column(TEXT, unique=False)
    
    horo_tomorrow = Column(TEXT, unique=False)
    
    horo_week = Column(TEXT, unique=True)
    
    horo_month = Column(TEXT, unique=True)
    
    horo_year = Column(TEXT, unique=True)
    
class Taro(BaseModel):
    __tablename__ = 'taro'
    
    name = Column(VARCHAR(32), unique=True, primary_key=True)
    
    silk = Column(TEXT)
    
    desc = Column(TEXT, unique=True)
    
class VostokHoro(BaseModel):
    __tablename__ = 'vostok'
    
    name = Column(VARCHAR(32), unique=True, primary_key=True)
    
    desc = Column(TEXT, unique=True)
    
class NumberMagic(BaseModel):
    __tablename__ = 'number'
    
    id = Column(INTEGER, unique=True, primary_key=True)
    
    desc = Column(TEXT, unique=True)

class Compatibility(BaseModel):
    __tablename__ = 'compatibility'
    
    id = Column(INTEGER, unique=True, primary_key=True)
    
    first_zodiac = Column(VARCHAR(32), unique=False)
    
    second_zodiac = Column(VARCHAR(32), unique=False)
    
    desc = Column(TEXT, unique=True)
    
class Channel(BaseModel):
    __tablename__ = 'channel'
    
    id = Column(INTEGER, unique=True, primary_key=True)
    
    silk = Column(TEXT)
    
    id_channel = Column(VARCHAR(32), unique=False)