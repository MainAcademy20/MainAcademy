from peewee import SqliteDatabase, Model, CharField, ForeignKeyField, PrimaryKeyField
import logging

logging.basicConfig(level=logging.DEBUG)

db = SqliteDatabase('candidates.db')


class BaseModel(Model):
    class Meta:
        database = db


class Candidates_list(BaseModel):
    last_name = CharField()
    first_name = CharField()
    status = CharField()

class Text(BaseModel):
    list_ = ForeignKeyField(Candidates_list, related_name='candidates')
    text = CharField()
