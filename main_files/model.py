import sqlite3
import random


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


def func_random_words():
    con = sqlite3.connect('words.db')
    cur = con.cursor()
    cur.execute('SELECT id_word FROM words')
    m = list()
    for i in cur:
        g = i[0]
        m.append(g)
    for _ in range(1):
        h = random.choice(m)
        try:
            cur.execute('SELECT eng_word FROM words WHERE id_word = {}'.format(h))
        except sqlite3.DatabaseError as err:
            print("Error", err)
        else:
            for i in cur:
                g = i[0]
                return g
