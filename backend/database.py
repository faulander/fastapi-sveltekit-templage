from peewee import SqliteDatabase
import os

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'shared', 'app.db')
db = SqliteDatabase(db_path)
