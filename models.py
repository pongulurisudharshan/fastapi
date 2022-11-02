from sqlalchemy import Column, Integer, str
from .database import Base # we are import the module base from the database.py file 
#here database works like a module 


class Blog(Base):
    __tablename__= 'blogs'
    id=Column(Integer,primary_key=True,index=True)
    title=Column(str)
    body=Column(str)