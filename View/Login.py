# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QDialog, QMessageBox

from Sistema.Test import Test
#from Main.InterfacciaMain import InterfacciaMain
from View.Main import Main


class Ui_Login(QDialog):

    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(400, 300)
        self.label_username = QtWidgets.QLabel(Login)
        self.label_username.setGeometry(QtCore.QRect(20, 20, 121, 18))
        self.label_username.setObjectName("label_username")
        self.label_password = QtWidgets.QLabel(Login)
        self.label_password.setEnabled(True)
        self.label_password.setGeometry(QtCore.QRect(20, 80, 111, 18))
        self.label_password.setObjectName("label_password")
        self.line_username = QtWidgets.QLineEdit(Login)
        self.line_username.setGeometry(QtCore.QRect(110, 10, 211, 36))
        self.line_username.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.line_username.setObjectName("line_username")
        self.line_password = QtWidgets.QLineEdit(Login)
        self.line_password.setGeometry(QtCore.QRect(110, 70, 211, 36))
        self.line_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.line_password.setObjectName("line_password")
        self.btn_accedi = QtWidgets.QPushButton(Login)
        self.btn_accedi.setGeometry(QtCore.QRect(130, 160, 151, 51))
        self.btn_accedi.setObjectName("btn_accedi")
        self.btn_accedi.clicked.connect(self.controllo)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.label_username.setText(_translate("Login", "Username:"))
        self.label_password.setText(_translate("Login", "Password:"))
        self.btn_accedi.setText(_translate("Login", "Accedi"))

    def controllo(self):
        if self.line_username.text() == "admin" and self.line_password.text()== "admin":
            self.main = Main()
            #self.main.show()
            self.close()
        else:
            QMessageBox.critical(self, "Accesso negato", "RIPROVA SE HAI IL CORAGGIO")

if __name__ == "__main__":
    import sys


    app = QtWidgets.QApplication(sys.argv)
    test = Test()
    test.controllo_fumetto()
    Login = QtWidgets.QWidget()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec())
