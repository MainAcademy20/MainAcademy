import sqlite3
import peewee

from models import PhotoFiles


def get_all_photos():
    return PhotoFiles.select()


def insert_file(name):
    row = PhotoFiles(name=name, title='foto')
    row.save()


def delete_file(name):
    c = PhotoFiles.get(PhotoFiles.name == name)
    c.delete_instance()