import os
from flask import Flask, request, redirect, render_template, send_from_directory
from werkzeug.utils import secure_filename
from models import PhotoFiles
from controller import get_all_photos, insert_file, delete_file


UPLOAD_FOLDER = 'D:/ZaitsevaLenaPython/flask_tutorial/static' #lockalhost/static
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'gif'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            insert_file(file.filename)
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template('upload.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)





@app.route('/photoload.html')
def gallery():
    items = get_all_photos()
    return render_template('photoload.html', spisok=items)


@app.route('/fotodel')
def fotodel():
    dfile = request.args['del']
    delete_file(dfile)
    items = get_all_photos()
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], dfile))
    return render_template('photoload.html', spisok=items)


if __name__ == "__main__":
    app.run()