from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import Qt

class Main_Window(Qt.QMainWindow):
    def __init__(self):
        Qt.QMainWindow.__init__(self)
        self.tab = Qt.QTabWidget()
        self.setCentralWidget(self.tab)

        self.btnOpen = Qt.QPushButton('Open')
        self.btnOpen.clicked.connect(self.open_file)
        self.statusBar().addWidget(self.btnOpen)

        self.btnClose = Qt.QPushButton('Close')
        self.btnClose.clicked.connect(self.close_file)
        self.statusBar().addWidget(self.btnClose)

    def open_file(self):
        file_name = Qt.QFileDialog.getOpenFileName()[0]
        if not file_name: return
        with open(file_name) as f:
            txt = f.read()
        idx = self.tab.addTab(Qt.QTextEdit(), file_name)
        self.tab.widget(idx).setPlainText(txt)
        self.tab.setCurrentIndex(idx)

    def save_changes(self):
        file_name = Qt.QFileDialog.getSaveFileName()[0]
        if not file_name: return
        txt = self.tab.currentWidget().toPlainText()
        with open(file_name, 'w') as f:
            f.write(txt)

    def close_file(self):
        index = self.tab.currentIndex()
        wiget = self.tab.widget(index)
        self.tab.removeTab(index)
        del wiget

if __name__ == "__main__":
    app = Qt.QApplication([])
    t = Main_Window()
    t.resize(1280, 720)
    t.show()
    app.exec_()
