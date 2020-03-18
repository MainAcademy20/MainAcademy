from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Main_Window(QWidget):
    def __init__(self):
        """"создает окно с деревом системы для поиска и открытия нужного документа """
        super().__init__()
        self.topLay = QHBoxLayout(self)
        self.splitter = QSplitter(self)
        self.topLay.addWidget(self.splitter)
        self.model = QFileSystemModel(self)
        """дерево с основным путем"""
        self.model.setRootPath(QDir.currentPath())
        self.tree = QTreeView(self.splitter)
        self.tree.setModel(self.model)
        """разделяет выпадающее окно на колонку с "деревом" и рабочим полем"""
        cur = self.model.index(QDir.currentPath())
        #self.tree.setCurrentIndex(cur) """открывает папку откуда вызываем приложение"""
        self.tree.expand(cur)
        self.view = QWidget()
        self.splitter.addWidget(self.tree)
        self.splitter.addWidget(self.view)
        """помещает древо в отдельную колонку"""
        self.tree.setColumnWidth(0, 200)
        """вызывает окнов  максимальном разрешении"""
        self.setWindowState(Qt.WindowMaximized)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    w = Main_Window()
    w.show()
    sys.exit(app.exec_())

