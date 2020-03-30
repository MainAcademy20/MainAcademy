from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import Qt


class Main_Window(QWidget):

    def __init__(self):
        super().__init__()

    def mainwindow(self):
        self.topLay = QHBoxLayout(self)
        self.splitter = QSplitter(self)
        self.topLay.addWidget(self.splitter)
        """self.topLay.addWidget(self.edit_line)"""
        self.model = QFileSystemModel(self)
        self.model.setRootPath(QDir.currentPath())
        self.tree = QTreeView(self.splitter)
        self.tree.doubleClicked.connect(self.selected_item)
        self.tree.setModel(self.model)
        cur = self.model.index(QDir.currentPath())
        self.tree.expand(cur)
        self.tree.setColumnWidth(0, 200)
        self.view = Qt.QTabWidget()
        self.splitter.addWidget(self.tree)
        self.splitter.addWidget(self.view)
        self.show()

    """def edit_line(self):
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
        self.topLay(grid)"""

    def selected_item(self, signal):
        file_path = self.model.filePath(signal)
        with open(file_path) as f:
            txt = f.read()
        idx = self.view.addTab(Qt.QTextEdit(), file_path)
        self.view.widget(idx).setPlainText(txt)
        self.view.setCurrentIndex(idx)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    w = Main_Window()
    w.resize(1440, 900)
    w.show()
    sys.exit(app.exec_())