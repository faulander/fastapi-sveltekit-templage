from peewee import Model, CharField
from database import db

class Settings(Model):
    key = CharField()
    value = CharField()

    class Meta:
        database = db
