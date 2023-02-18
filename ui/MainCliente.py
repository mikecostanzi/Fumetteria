from PyQt6 import uic
from PyQt6.QtWidgets import QWidget


class MainCliente(QWidget):
    def __init__(self):
        super(MainCliente,self).__init__()
        uic.loadUi("main-cliente.ui",self)

        self.show()
