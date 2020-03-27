import os

from flask import Flask, render_template, request, redirect, url_for

from peewee import *


#os.mkdir('uploads')


MAX_FILE_SIZE = 1024 * 1024 + 1

app = Flask(__name__)


db = SqliteDatabase('photo.db')# ********models#


#*****************************************models*****#


class BaseModel(Model):
    class Meta:
        database = db


class PhotoFiles(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField()
    title = CharField()
    #title = CharField()


#**********************************controler************#

def get_all_photos():
    return PhotoFiles.select()


def insert_file(name):
    row = PhotoFiles(name=name, title='foto')
    row.save()
    #PhotoFiles.create(name=name)

#**************************************************#


@app.route("/", methods=["POST", "GET"])
def index():
    args = {"method": "GET"}
    if request.method == "POST":
        file = request.files["file"]
        if bool(file.filename):
            file_bytes = file.read(MAX_FILE_SIZE)
            args["file_size_error"] = len(file_bytes) == MAX_FILE_SIZE
        args["method"] = "POST"
        insert_file(file.filename)
    return render_template("index.html", args=args)


@app.route('/photoload.html')
def gallery():
    items = get_all_photos()
    return render_template('photoload.html', spisok=items)


#PhotoFiles.create_table()






if __name__ == "__main__":
    app.run(debug=True)