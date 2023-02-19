from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from ui.InserimentoCliente import InserimentoCliente


class MainCliente(QWidget):
    def __init__(self):
        super(MainCliente,self).__init__()
        uic.loadUi("main-cliente.ui",self)
        self.btn_inserisci.clicked.connect(self.go_inserimento_cliente)
        self.show()
    def go_inserimento_cliente(self):
        self.inserimento_cliente = InserimentoCliente()
        self.inserimento_cliente.show()