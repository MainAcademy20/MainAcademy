from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import Qt


class Main_Window(QWidget):

    def __init__(self):
        """"создает окно с деревом системы для поиска и открытия нужного документа """
        super().__init__()

    def mainwindow(self):
        self.topLay = QHBoxLayout(self)
        self.splitter = QSplitter(self)
        self.topLay.addWidget(self.splitter)
        """пытаюсь добавить новый виджет в котором будут заполнятся данные кандидатов"""
        self.splitter2 = QSplitter(self.Qt.Horizontal)
        self.top = QFrame(self)
        self.top.setFrameShape(QFrame.StyledPanel)
        self.splitter2.addWidget(self.top)
        self.topLay.addWidget(self.splitter2)
        """конец кода виджета"""
        self.model = QFileSystemModel(self)
        """дерево с основным путем"""
        self.model.setRootPath(QDir.currentPath())
        self.tree = QTreeView(self.splitter)
        self.tree.doubleClicked.connect(self.selected_item)
        self.tree.setModel(self.model)
        """разделяет выпадающее окно на колонку с "деревом" и рабочим полем"""
        cur = self.model.index(QDir.currentPath())
        #self.tree.setCurrentIndex(cur) """открывает папку откуда вызываем приложение"""
        self.tree.expand(cur)
        self.tree.setColumnWidth(0, 200)
        self.view = Qt.QTabWidget()
        self.splitter.addWidget(self.tree)
        self.splitter.addWidget(self.view)


    """ Виджет для заполнения имени и фамилии кандидата
    def candidate(self):
        self.splitter2 = QSplitter(self)
        self.topLay.addWidget(self.splitter2)
        firstname = QLabel('First Name')
        lastname = QLabel('Last Name')

        firstnameEdit = QLineEdit()
        lastnameEdit = QLineEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(firstname, 1, 0)
        grid.addWidget(firstnameEdit, 1, 1)

        grid.addWidget(lastname, 2, 0)
        grid.addWidget(lastnameEdit, 2, 1)

        self.setLayout(grid)
        self.show()"""

    def selected_item(self, signal):
        file_path = self.model.filePath(signal)
        print(file_path)
        with open(file_path) as f:
            txt = f.read()
        idx = self.view.addTab(Qt.QTextEdit(), file_path)
        self.view.widget(idx).setPlainText(txt)
        self.view.setCurrentIndex(idx)


if __name__ == '__main__':
    import sys

    app = QApplication([])
    w = Main_Window()
    w.resize(1440, 900)
    w.show()
    sys.exit(app.exec_())