from app import app
from flask import render_template

@app.route("/")
def main():
    return "Hello world. <a href='/page1'>Go to page 1</a>"

@app.route("/page1")
def page1():
    return "Page 1 contetn."

@app.route("/hello/<username>")
def hello(username):
    return render_template("hellouser.html", name=username)
if __name__ == "__main__":
    app.run()