import sqlite3
from flask import Flask

app = Flask('my shop')


@app.route('/')
def index():
    return render_templates('index.html')
app.run(debug=True)

@app.route('/create-item')
def create_item():
    return "OK"



def insert_item():
    query = """
    INSERT INTO product
    VALUES 'test', 123
    """
    conn = sqlite3.connect("shop.db")
    conn.execute(query)
    conn.commit()