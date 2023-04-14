from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from View.InserimentoCliente import InserimentoCliente
from View.MainTessera import MainTessera
from View.RicercaClienti import RicercaClienti


class RicercaCliente:
    pass


class MainCliente(QWidget):
    def __init__(self):
        super(MainCliente,self).__init__()
        uic.loadUi('../ui/main-cliente.ui',self)
        self.btn_inserisci.clicked.connect(self.go_inserisci_cliente)
        self.btn_ricerca.clicked.connect(self.go_ricerca_cliente)
        self.btn_tessere.clicked.connect(self.go_tessere)
    def go_inserisci_cliente(self):
        self.inserisci_cliente = InserimentoCliente()
        self.inserisci_cliente.show()
    def go_ricerca_cliente(self):
        self.ricerca_cliente = RicercaClienti()
        self.ricerca_cliente.show()
    def go_tessere(self):
        self.main_tessere = MainTessera()
        self.main_tessere.show()