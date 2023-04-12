from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from View.InserimentoCliente import InserimentoCliente


class MainCliente(QWidget):
    def __init__(self):
        super(MainCliente,self).__init__()
        uic.loadUi('../ui/main-cliente.ui',self)
        self.btn_inserisci.clicked.connect(self.go_inserisci_cliente)

    def go_inserisci_cliente(self):
        self.inserisci_cliente = InserimentoCliente()
        self.inserisci_cliente.show()