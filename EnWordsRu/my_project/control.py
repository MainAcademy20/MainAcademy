from EnWordsRu import view, model


def clicked_btn_wr():
    view.MainWindow.open_second_win = view.WriteWindow()
    view.MainWindow.open_second_win.write_win.show()


def clicked_btn_re():
    view.MainWindow.open_second_win = view.RepeateWindow()
    view.MainWindow.open_second_win.repeate_win.show()


def click_clean_w():
    view.MainWindow.open_second_win.ru_word.clear()
    view.MainWindow.open_second_win.en_word.clear()


def click_save_w():
    en_word = view.MainWindow.open_second_win.en_word.text()
    ru_word = view.MainWindow.open_second_win.ru_word.text()
    words = (en_word, ru_word)
    model.write_db(words)
