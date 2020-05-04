from main_files import view, model
from PyQt5 import QtGui


def clicked_btn_wr_M():
    view.MainWindow.open_second_win = view.WriteWindow()
    view.MainWindow.open_second_win.write_win.show()
    model.add_txt_to_label()


def clicked_btn_re_M():
    view.MainWindow.open_second_win = view.RepeateWindow()
    view.MainWindow.open_second_win.repeate_win.show()


def click_save_W():
    en_word = view.MainWindow.open_second_win.en_word.text()
    ru_word = view.MainWindow.open_second_win.ru_word.text()
    words = (en_word, ru_word)
    if en_word != '' and ru_word != '':
        model.write_db(words)
    view.MainWindow.open_second_win.ru_word.clear()
    view.MainWindow.open_second_win.en_word.clear()
    model.add_txt_to_label()


def click_btn_del_W():
    model.delete_word()
    model.add_txt_to_label()


def click_btn_start_R():
    en_ru = model.func_random_words()
    view.MainWindow.open_second_win.random_word.setText('<h1>{}</h2>'.format(en_ru[0][0]))
    view.MainWindow.open_second_win.save_word.setText(en_ru[0][0])
    view.MainWindow.open_second_win.btn_start.setDisabled(True)
    view.MainWindow.open_second_win.btn_answer.setDisabled(False)


def click_btn_send_R():
    medium = model.check_correct_answer()
    if medium == '+':
        view.MainWindow.open_second_win.check_answer.setPixmap(QtGui.QPixmap('../main_files/images/right.jpg'))
    else:
        view.MainWindow.open_second_win.check_answer.setPixmap(QtGui.QPixmap('../main_files/images/wrong.jpg'))
    view.MainWindow.open_second_win.user_enter.clear()
    en_ru = model.func_random_words()
    view.MainWindow.open_second_win.random_word. \
        setText('<h1>{}</h2>'.format(en_ru[0][0]))
    view.MainWindow.open_second_win.save_word.setText(en_ru[0][0])


def check_user_enter():
    english_w = view.MainWindow.open_second_win.save_word.text()
    russian_w = view.MainWindow.open_second_win.user_enter.text()
    return russian_w, english_w
