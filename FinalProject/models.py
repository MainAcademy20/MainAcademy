
from peewee import SqliteDatabase, Model
from peewee import *

db = SqliteDatabase('photo.db')


class BaseModel(Model):
    class Meta:
        database = db


class PhotoFiles(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField()
    title = CharField()


if __name__ == '__main__':
    db.create_tables([PhotoFiles])
