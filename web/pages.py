from flask import render_template

from app import app


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/page1')
def page1():
    return 'Page1 content <p> <a href="/">Main page</a> </p>'


@app.route('/hello/<username>')
def hello(username):
    return render_template('hellouser.html', name=username)


@app.route('/entry')
def entry():
    return render_template('entry.html')


if __name__ == '__main__':
    app.run()
