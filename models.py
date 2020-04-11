from peewee import SqliteDatabase, Model, CharField, ForeignKeyField, PrimaryKeyField
import logging

logging.basicConfig(level=logging.DEBUG)

db = SqliteDatabase('candidates.db')


class BaseModel(Model):
    class Meta:
        database = db


class List(BaseModel):
    name = CharField()


class Candidates(BaseModel):
    list_ = ForeignKeyField(List, related_name='texts')
    candidates_ = CharField()