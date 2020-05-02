from main_files import view, model


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
    view.MainWindow.open_second_win.random_word.\
            setText(model.func_random_words())
    view.MainWindow.open_second_win.btn_start.setDisabled(True)


def click_btn_send_R():
    medium = model.check_correct_answer()
    if medium == '+':
        view.MainWindow.open_second_win.check_answer.setText('Right')
    else:
        view.MainWindow.open_second_win.check_answer.setText('Wrong')
    view.MainWindow.open_second_win.user_enter.clear()
    view.MainWindow.open_second_win.random_word.\
        setText(model.func_random_words())


def check_user_enter():
    english_w = view.MainWindow.open_second_win.random_word.text()
    russian_w = view.MainWindow.open_second_win.user_enter.text()
    return english_w, russian_w