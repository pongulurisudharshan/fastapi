from fileinput import close
from gc import get_debug
from msilib import schema
from turtle import title
from wsgiref.util import request_uri#here we import title from turtle module to represent the title
from fastapi import FastAPI#fastapi module is used to create the app
import uvicorn#uvicorn module used to create the server for our fastapi application
from pydantic import BaseModel#basemodel from pydantics it will create the requests very easy mode
import schemas#schemas is userdefined module 
import models
from .database import engine,SessionLocal
from sqlalchemy.orm  import Session
app=FastAPI()


models.Base.metadata.create_all(engine)

def get_db():
db= SessionLocal()
try:
    yield db
finally:
    db.close()
@app.post('/blog')

# @app-it is a decorator
# post-operation 
# /blog-it is a base server 
# here we are performing an operation on server using the decorator. 
#this blog is used to store the blog information into the database.
def create_blog(request: schemas.blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
 
#this below function is used to get all the blogs information from the database
@app.get('/blog')
def all(db: Session =Depends(get_db)):
    blogs= db.query(models.Blog).all()
    return blogs

if __name__=='__main__':
    uvicorn.run(app,host='0.0.0.0',port=8000)
#above line we mentioned the application name and host address and port number.