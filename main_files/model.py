from main_files import control, view
import sqlite3
import random
from PyQt5 import QtGui


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


def delete_word():
    con = sqlite3.connect('words.db')
    cur = con.cursor()
    try:
        cur.execute("DELETE FROM words WHERE id_word = (SELECT MAX(id_word) FROM words)")
    except sqlite3.DatabaseError as err:
        print("Error", err)
    else:
        con.commit()
    cur.close()
    con.close()


def func_random_words():
    con = sqlite3.connect('words.db')
    cur = con.cursor()
    sql = "SELECT eng_word, rus_word FROM words ORDER BY RANDOM() LIMIT 1"
    try:
        cur.execute(sql)
        rand_words = []
        for i in cur:
            rand_words.append(i)
    except sqlite3.DatabaseError as err:
        print('Error:', err)
    else:
        return rand_words
    cur.close()
    con.close()


def check_correct_answer():
    rus_word, eng_word = control.check_user_enter()
    con = sqlite3.connect('words.db')
    cur = con.cursor()
    try:
        cur.execute("SELECT rus_word FROM words WHERE eng_word = '{}'".format(eng_word))
        for i in cur:
            g = i[0]
            if g == rus_word:
                return '+'
    except sqlite3.DatabaseError as err:
        print('Error', err)
    cur.close()
    con.close()


def label_words():
    con = sqlite3.connect('words.db')
    cur = con.cursor()
    ru_words = list()
    en_words = list()
    try:
        cur.execute('SELECT * FROM words')
    except sqlite3.DatabaseError as err:
        print('Error:', err)
    else:
        for i in cur:
            en_word = i[1]
            en_words.append(en_word)
            ru_word = i[2]
            ru_words.append(ru_word)
    l = len(en_words)
    return en_words[l-1], en_words[l-2], en_words[l-3], en_words[l-4],\
           en_words[l-5], ru_words[l-1], ru_words[l-2], ru_words[l-3], \
           ru_words[l-4], ru_words[l-5]


def add_txt_to_label():
    list_words = label_words()
    k = 4
    for i in range(5):
        view.MainWindow.open_second_win.list_label[i].setText('<h4>{}</h4>'.format(list_words[k]))
        k -= 1
    m = 9
    for i in range(5, 10):
        view.MainWindow.open_second_win.list_label[i].setText('<h4>{}</h4>'.format(list_words[m]))
        m -= 1


