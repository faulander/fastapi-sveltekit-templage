from peewee import Model, CharField, DateTimeField
from database import db

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    created_at = DateTimeField(formats='%Y-%m-%d %H:%M:%S')

class Settings(BaseModel):
    key = CharField()
    value = CharField()
