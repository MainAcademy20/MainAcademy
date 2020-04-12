import os

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import Qt
from apscheduler.schedulers.background import BackgroundScheduler

from models import Candidates, db

scheduler = BackgroundScheduler()

db.create_tables([Candidates])

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1016, 864)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(1016, 813))
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(290, 70, 191, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(510, 70, 201, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 250, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 50, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(510, 50, 71, 16))
        self.label_2.setObjectName("label_2")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(10, 10, 271, 791))
        self.treeView.setObjectName("treeView")
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(990, 290, 22, 521))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(290, 220, 191, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 10, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1016, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_2.clicked.connect(self.open_file_path)
        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.currentPath())
        self.treeView.setModel(self.model)
        self.treeView.doubleClicked.connect(self.open_file_path)
        self.pushButton.clicked.connect(self.candidates)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(290, 300, 701, 501))
        self.textEdit.setObjectName("textEdit")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def open_file_path(self):
        file_path = self.model.filePath(self.treeView.currentIndex())

        if not os.path.isfile(file_path):
            return

        with open(file_path) as f:
            txt = f.read()
            self.textEdit.setPlainText(txt)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить"))
        self.label.setText(_translate("MainWindow", "Фамилия"))
        self.label_2.setText(_translate("MainWindow", "Имя"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Одобрен"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Откленен"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Принят на работу"))
        self.pushButton_2.setText(_translate("MainWindow", "Импорт"))

    def candidates(self):
        last_names = self.label_2()
        first_names = self.lineEdit()
        statuses = self.comboBox()
        candidate_ln = last_names
        candidate_value = candidate_ln.text()
        if not candidate_value:
            return
        current_list = Candidates_list.get(name=candidate_ln.currentText())
        Candidates_list.create(text=candidate_ln, list_=current_list)
        candidate_fn = first_names
        candidate_value1 = candidate_fn.text()
        if not candidate_value1:
            return
        current_list = Candidates_list.get(name=candidate_fn.currentText())
        Candidates_list.create(text=candidate_fn, list_=current_list)
        candidate_st = statuses
        candidate_st_value = statuses.text()
        if not candidate_st_value:
            return
        current_list = Candidates_list.get(name=candidate_st.currentText())
        Candidates_list.create(text=candidate_st, list_=current_list)




if __name__ == "__main__":
    import sys


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
