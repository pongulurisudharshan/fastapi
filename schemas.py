from pydantic import BaseModel
import sqlalchemy

class blog(BaseModel):
    title : str
    body : str