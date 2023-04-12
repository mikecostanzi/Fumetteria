from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox

from Controller.GestoreClienti import GestoreClienti


class InserimentoCliente(QWidget):

    def __init__(self):
        super(InserimentoCliente,self).__init__()
        uic.loadUi('../ui/inserimento-cliente.ui',self)
        self.btn_inserisci.clicked.connect(self.inserimento)


    def inserimento(self):
        id = int(self.line_id.text())
        nome = self.line_nome.text()
        cognome = self.line_cognome.text()
        indirizzo = self.line_indirizzo.text()
        telefono = self.line_telefono.text()
        email = self.line_email.text()
        codice = self.line_codice.text()
        data = (id,nome,cognome,indirizzo,telefono,email,codice)
        print(data)
        cliente = GestoreClienti()
        if  not id:
            QMessageBox.critical(self,'Errore','Inserisci i dati necessari')
        else:
            cliente.inserisci_cliente(id,nome,cognome,indirizzo,telefono,email,codice)
            print('Cliente inserito correttamente')

