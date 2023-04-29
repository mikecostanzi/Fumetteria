from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox

from Controller.GestoreClienti import GestoreClienti


class InserimentoCliente(QWidget):

    def __init__(self):
        super(InserimentoCliente,self).__init__()
        uic.loadUi('../ui/inserimento-cliente.ui',self)
        self.btn_inserisci.clicked.connect(self.inserimento)


    def inserimento(self):
        try:
            id = int(self.line_id.text())
            nome = self.line_nome.text()
            cognome = self.line_cognome.text()
            indirizzo = self.line_indirizzo.text()
            telefono = self.line_telefono.text()
            email = self.line_email.text()
            data = (id,nome,cognome,indirizzo,telefono,email,None)
            print(data)
            cliente = GestoreClienti()
            if id is None:
                QMessageBox.critical(self,'Errore','Inserisci i dati necessari')
            else:
                cliente.inserisci_cliente(id,nome,cognome,indirizzo,telefono,email,None)
                self.close()
                print('Cliente inserito correttamente')
        except Exception as m:
            QMessageBox.critical(self,'Errore','Inserisci i dati correttamente')
            print(m)
