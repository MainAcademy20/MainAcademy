import sqlite3


def write_db(couple_of_words:tuple):
    con = sqlite3.connect('words.db')
    cur = con.cursor()
    sql = 'INSERT INTO words (eng_word, rus_word) VALUES (?, ?)'
    try:
        cur.execute(sql, couple_of_words)
    except sqlite3.DatabaseError as err:
        print('Error', err)
    else:
        print('Successful')
        con.commit()
    cur.close()
    con.close()


def from_db():
    con = sqlite3.connect('words.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM words')
    for i in cur:
        print(i)

