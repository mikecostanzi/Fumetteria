from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from Controller.GestoreClienti import GestoreClienti


class ModificaCliente(QWidget):
    def __init__(self,id):
        super(ModificaCliente,self).__init__()
        uic.loadUi('../ui/modifica-cliente.ui',self)
        self.id = id
        self.btn_nome.clicked.connect(self.conferma_nome)
        self.btn_cognome.clicked.connect(self.conferma_cognome)
        self.btn_indirizzo.clicked.connect(self.conferma_indirizzo)
        self.btn_telefono.clicked.connect(self.conferma_telefono)
        self.btn_email.clicked.connect(self.conferma_email)
        self.btn_chiudi.clicked.connect(self.close)
        self.setWindowTitle(f'ID Cliente da modificare: {self.id}' )

    def conferma_nome(self):
        self.nome = self.line_nome.text()
        gestore = GestoreClienti()
        gestore.modifica_nome(self.id,self.nome)
    def conferma_cognome(self):
        self.cognome = self.line_cognome.text()
        gestore = GestoreClienti()
        gestore.modifica_cognome(self.id,self.cognome)
    def conferma_indirizzo(self):
        self.indirizzo = self.line_indirizzo.text()
        gestore = GestoreClienti()
        gestore.modifica_indirizzo(self.id,self.indirizzo)
    def conferma_telefono(self):
        self.telefono = self.line_telefono.text()
        gestore = GestoreClienti()
        gestore.modifica_telefono(self.id,self.telefono)
    def conferma_email(self):
        self.email = self.line_email.text()
        gestore = GestoreClienti()
        gestore.modifica_email(self.id,self.email)