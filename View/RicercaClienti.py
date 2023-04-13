from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget, QMessageBox

from Controller.GestoreClienti import GestoreClienti
from Model.Cliente import Cliente
from View.VistaCliente import VistaCliente


class RicercaClienti(QWidget):
    def __init__(self):
        super(RicercaClienti,self).__init__()
        uic.loadUi('../ui/ricerca-clienti.ui',self)
        self.lista = []
        self.btn_cerca.clicked.connect(self.inserimento_codice)
        self.btn_apri.clicked.connect(self.apri_cliente)
    def inserimento_codice(self):
        try:
            gestore_clienti = GestoreClienti()
            cliente = gestore_clienti.ricerca_cliente(self.line_barra.text())

            lista_model = QStandardItemModel(self.lista_clienti)

            for elemento in cliente:
                item = QStandardItem()
                riga = f'ID:{elemento[0]} - Nome: {elemento[1]} - Cognome: {elemento[2]} - Codice: {elemento[6]}'
                print(riga)
                item.setText(riga)
                item.setEditable(False)
                font = item.font()
                font.setPixelSize(18)
                item.setFont(font)
                lista_model.appendRow(item)
            self.lista_clienti.setModel(lista_model)
        except Exception as m:
            QMessageBox.critical(self,'Errore','Il cliente non esiste')
            print(m)
    def apri_cliente(self):
        try:
            selected = self.lista_clienti.selectedIndexes()[0].data()
            id = (selected.split('-')[0].strip().split(':')[1])
            print('id selezionato è: '+id)
            gestore = GestoreClienti()
            cliente_ricercato = gestore.ricerca_cliente(id)
            self.go_vista_cliente = VistaCliente(cliente_ricercato)
            self.go_vista_cliente.show()
        except Exception as m:
            print(m)
