from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
#here we declaring a mapping like class variable to table column names
from sqlalchemy.orm import sessionmaker
#here we are creating the seassionmaker to create the session for fastapi

sqlite1='sqlite:///./blog.db'
#in this blog.db is my sqlite3 database 
#i stored (or) assigned the database location path into the sqlite1 variable
engine= create_engine(sqlite1,connect_args={"check_same_thread": False})
#then i have created a engine which is used to make a connection between the database to our code fastapi 
#and we are using the connection args as false.
SessionLocal = sessionmaker(bind=engine, autocommit= False, autoflush=False)
#here we assigned the sessionmaker to userdefined variable called sessionlocal
Base= declarative_base()
#here base is works like mapping .