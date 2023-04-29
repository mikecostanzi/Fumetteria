from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox

from Controller.GestoreClienti import GestoreClienti
from Controller.GestoreTessere import GestoreTessere
from Model.Cliente import Cliente


class InserimentoTessera(QWidget):
    def __init__(self,cliente):
        super(InserimentoTessera, self).__init__()
        uic.loadUi('../ui/inserimento-tessera.ui', self)
        for dato in cliente:
            self.c = Cliente(dato[0],dato[1],dato[2],dato[3],dato[4],dato[5],dato[6])
        self.l_id.setText(f'Cliente ID: {self.c.get_id()}')
        self.l_nome.setText(f'Nome: {self.c.get_nome()}')
        self.l_cognome.setText(f'Cognome: {self.c.get_cognome()}')
        self.l_indirizzo.setText(f'Indirizzo: {self.c.get_indirizzo()}')
        self.l_telefono.setText(f'Telefono: {self.c.get_telefono()}')
        self.l_email.setText(f'Email: {self.c.get_email()}')

        self.btn_inserisci.clicked.connect(self.inserimento)
        self.setWindowTitle('Inserimento di una tessera')


    def inserimento(self):
        try:
            codice = int(self.line_codice.text())
            data_inizio = self.line_data.text()
            punti = int(self.line_punti.text())
            tessera = GestoreTessere()
            cliente = GestoreClienti()
            if codice is None:
                QMessageBox.critical(self, 'Errore', 'Inserisci i dati necessari')
            else:
                tessera.inserisciTessera(codice,data_inizio,punti)
                cliente.modifica_codice(self.c.get_id(),codice)
                self.close()
                print('Tessera inserita correttamente')
        except Exception as m:
            QMessageBox.critical(self,'Errore','Inserisci i dati correttamente')
            print(m)