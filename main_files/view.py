from PyQt5 import QtWidgets, QtCore, QtGui
from main_files import control


class MainWindow(QtWidgets.QWidget):
    open_second_win = None

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.build()
        self.signals()

    def build(self):
        self.resize(500, 300)
        self.setWindowTitle('EnWordsRu')
        self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        icon = QtGui.QIcon('../main_files/images/Logo1.jpg')
        self.setWindowIcon(icon)
        self.btn_write = QtWidgets.QPushButton('Writing')
        self.btn_repeate = QtWidgets.QPushButton('Repeating')
        wr_label = QtWidgets.QLabel('Режим записи выученых слов.\nНажмите чтобы перейти!')
        rp_label = QtWidgets.QLabel('Режим повторения выученых слов.\nНажмите чтобы перейти!')
        self.grid = QtWidgets.QGridLayout()
        self.grid.addWidget(wr_label, 1, 0, 3, 1)
        self.grid.addWidget(rp_label, 1, 1, 3, 1)
        self.grid.addWidget(self.btn_write, 0, 0, 3, 1)
        self.grid.addWidget(self.btn_repeate, 2, 1, 3, 1)
        self.setLayout(self.grid)

    def signals(self):
        self.btn_write.clicked.connect(control.clicked_btn_wr_M)
        self.btn_repeate.clicked.connect(control.clicked_btn_re_M)


class WriteWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.build()
        self.signals()

    def build(self):
        self.write_win = QtWidgets.QWidget()
        self.write_win.resize(600, 300)
        self.write_win.setWindowTitle('EnWordsRu')
        self.write_win.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.write_win.setWindowModality(QtCore.Qt.ApplicationModal)
        icon = QtGui.QIcon('../main_files/images/Logo1.jpg')
        self.write_win.setWindowIcon(icon)
        self.grid = QtWidgets.QGridLayout()
        self.en_word = QtWidgets.QLineEdit()
        self.ru_word = QtWidgets.QLineEdit()
        self.btn_save = QtWidgets.QPushButton('Save words')
        self.btn_delete = QtWidgets.QPushButton('Delete last word')
        self.list_label = list()
        for _ in range(10):
            lbl = QtWidgets.QLabel()
            self.list_label.append(lbl)
        k = 0
        for i in range(5):
            self.grid.addWidget(self.list_label[i], k, 0, 1, 1,QtCore.Qt.AlignHCenter)
            k += 1
        m = 0
        for i in range(5, 10):
            self.grid.addWidget(self.list_label[i], m, 1, 1, 1,QtCore.Qt.AlignHCenter)
            m += 1
        self.grid.addWidget(self.en_word, 5, 0, 6, 1)
        self.grid.addWidget(self.ru_word, 5, 1, 6, 1)
        self.grid.addWidget(self.btn_save, 6, 0, 6, 1)
        self.grid.addWidget(self.btn_delete, 6, 1, 6, 1)
        self.write_win.setLayout(self.grid)

    def signals(self):
        self.btn_save.clicked.connect(control.click_save_W)
        self.btn_delete.clicked.connect(control.click_btn_del_W)


class RepeateWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.build()
        self.signals()

    def build(self):
        self.repeate_win = QtWidgets.QWidget()
        self.repeate_win.resize(600, 300)
        self.repeate_win.setWindowTitle('EnWordsRu')
        self.repeate_win.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.repeate_win.setWindowModality(QtCore.Qt.ApplicationModal)
        icon = QtGui.QIcon('../main_files/images/Logo1.jpg')
        self.repeate_win.setWindowIcon(icon)
        self.random_word = QtWidgets.QLabel()
        self.user_enter = QtWidgets.QLineEdit()
        self.check_answer = QtWidgets.QLabel(' ')
        self.save_word = QtWidgets.QLabel()
        self.btn_answer = QtWidgets.QPushButton('Send answer')
        self.btn_answer.setDisabled(True)
        self.btn_start = QtWidgets.QPushButton('Start')
        self.grid = QtWidgets.QGridLayout()
        self.grid.addWidget(self.check_answer, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.grid.addWidget(self.random_word, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.grid.addWidget(self.btn_start, 2, 0, 2, 1)
        self.grid.addWidget(self.user_enter, 1, 0, 2, 2)
        self.grid.addWidget(self.btn_answer, 2, 1, 2, 1)
        self.repeate_win.setLayout(self.grid)

    def signals(self):
        self.btn_start.clicked.connect(control.click_btn_start_R)
        self.btn_answer.clicked.connect(control.click_btn_send_R)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())