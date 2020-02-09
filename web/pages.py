from flask import render_template
from web_app import  app

@app.route('/')
def main() :
    return 'Hello world. <a href="/page1">Go to page1</a>'

@app.route('/page1')
def page1() :
    return 'page 1 content. <a href="/">Back</a>'

@app.route('/Hello/<username>')
def hello(username):
    return render_template('HelloUser.html' , name = username)

if __name__ == '__main__' :
    app.run()

