from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from Controller.GestoreCliente import GestoreCliente


class InserimentoCliente(QWidget):

    def __init__(self):
        super(InserimentoCliente,self).__init__()
        uic.loadUi("inserisci-cliente.ui",self)
        #self.btn_inserisci.clicked.connect()
        self.show()
    def inserimento_dati(self,idCliente,nome,cognome,dataNascita,indirizzo,telefono,email):
        self.inserisci = GestoreCliente()
        self.inserisci.inserisci_Cliente(idCliente,nome,cognome,dataNascita,indirizzo,telefono,email)
