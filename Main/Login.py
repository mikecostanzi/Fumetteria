from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QDialog
from Main.InterfacciaMain import InterfacciaMain
class Login(QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)

        l = QGridLayout()
        dato1 = QLabel('Username:')
        self.username = QLineEdit()
        l.addWidget(dato1,0,0)
        l.addWidget(self.username,0,1)
        dato2 = QLabel('Password:')
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        l.addWidget(dato2,1,0)
        l.addWidget(self.password,1,1)
        b = QPushButton("Accedi")
        b.clicked.connect(self.controllo)
        l.addWidget(b,2,0,2,1)
        self.setLayout(l)
        self.resize(200,200)
        self.setWindowTitle("Login")

    def controllo(self):
        if self.username.text() == "admin" and self.password.text() == "admin":
            self.interfaccia_main = InterfacciaMain()
            self.interfaccia_main.show()
            self.close()
        else:
            QMessageBox.critical(self,"Accesso negato", "RIPROVA SE HAI IL CORAGGIO",QMessageBox.Ok,QMessageBox.Ok)

