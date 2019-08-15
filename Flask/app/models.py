from sqlalchemy import Column, Integer, String
from .database import Base, db_session

class WebAPI(Base):
    __tablename__ = 'web_api'
    id = Column(Integer, primary_key=True)
    data = Column(String(100))

    def __init__(self, data):
        self.data = data

    @classmethod
    def save(cls, data):
        web = cls(data)
        db_session.add(web)
        db_session.commit()

    @classmethod
    def getAll(cls):
        web_api_data = cls.query.all()
        # print(web_api_data)
        return web_api_data
        
