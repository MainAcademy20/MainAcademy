from PyQt5 import QtWidgets, QtCore, QtGui
from EnWordsRu import control


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
        icon = QtGui.QIcon('Logo1.jpg')
        self.setWindowIcon(icon)
        self.btn_write = QtWidgets.QPushButton('Writing')
        self.btn_repeate = QtWidgets.QPushButton('Repeating')
        self.grid = QtWidgets.QGridLayout()
        self.grid.addWidget(self.btn_write, 0, 0, 2, 1)
        self.grid.addWidget(self.btn_repeate, 2, 2, 2, 1)
        self.setLayout(self.grid)

    def signals(self):
        self.btn_write.clicked.connect(control.clicked_btn_wr)
        self.btn_repeate.clicked.connect(control.clicked_btn_re)


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
        icon = QtGui.QIcon('Logo1.jpg')
        self.write_win.setWindowIcon(icon)
        self.grid = QtWidgets.QGridLayout()
        self.en_word = QtWidgets.QLineEdit()
        self.ru_word = QtWidgets.QLineEdit()
        self.btn_save = QtWidgets.QPushButton('Save words')
        self.btn_clean = QtWidgets.QPushButton('Clean words')
        self.grid.addWidget(self.en_word, 0, 0)
        self.grid.addWidget(self.ru_word, 0, 1)
        self.grid.addWidget(self.btn_save, 1, 0)
        self.grid.addWidget(self.btn_clean, 1, 1)
        self.write_win.setLayout(self.grid)

    def signals(self):
        self.btn_clean.clicked.connect(control.click_clean_w)
        self.btn_save.clicked.connect(control.click_save_w)


class RepeateWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.build()

    def build(self):
        self.repeate_win = QtWidgets.QWidget()
        self.repeate_win.resize(600, 600)
        self.repeate_win.setWindowTitle('EnWordsRu')
        self.repeate_win.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.repeate_win.setWindowModality(QtCore.Qt.ApplicationModal)
        icon = QtGui.QIcon('Logo1.jpg')
        self.repeate_win.setWindowIcon(icon)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())