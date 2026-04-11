from sqlalchemy import Column, Integer , String
from database import Base

class APIkey(Base):
     __tablename__ = "api_key"

     id = Column(Integer,primary_key=True, index=True)

     key = Column(String, unique= True , index=True)

