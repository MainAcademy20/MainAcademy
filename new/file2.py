import sqlite3

conn = sqlite3.connect("shop.db")


def create_user():


def create_product():
    query = """
    CREATE TABLE product(
    name VARCHAR(30)
    prize DECIMAL
    )
    """

    conn.execute(query)
    conn.commit()

if __name__ = '__main__':
    create_product_table()