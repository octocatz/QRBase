from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime


class QRinfo(Base):
    __tablename__ = 'qrinfo'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    title = Column(Text)
    createdate = Column(DateTime, default=datetime.now())
    urlrandom = Column(Text)
    imgflg = Column(Integer)

    def __init__(self, name=None, title=None, createdate=None, urlrandom=None, imgflg=None):
        self.name = name
        self.title = title
        self.createdate = createdate
        self.urlrandom = urlrandom
        self.imgflg = imgflg

    def __repr__(self):
        return '<Title %r>' % (self.title)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(128), unique=True)
    hashed_password = Column(String(128))

    def __init__(self, user_name=None, hashed_password=None):
        self.user_name = user_name
        self.hashed_password = hashed_password

    def __repr__(self):
        return '<Name %r>' % (self.user_name)
