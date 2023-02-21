from PyQt6 import uic
from PyQt6.QtWidgets import QWidget




class InserimentoCliente(QWidget):

    def __init__(self):
        super(InserimentoCliente,self).__init__()
        uic.loadUi("inserisci-cliente.ui",self)
        #self.btn_inserisci.clicked.connect()
        self.show()
    def inserimento_dati(self,idCliente,nome,cognome,dataNascita,indirizzo,telefono,email):
        pass

