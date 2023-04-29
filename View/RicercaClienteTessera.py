from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget, QMessageBox

from Controller.GestoreClienti import GestoreClienti
from View.InserimentoTessera import InserimentoTessera


class RicercaClienteTessera(QWidget):
    def __init__(self):
        super(RicercaClienteTessera,self).__init__()
        uic.loadUi('../ui/ricerca-cliente-tessera.ui',self)
        self.gestore_clienti = GestoreClienti()
        self.btn_cerca.clicked.connect(self.inserimento_nome)
        self.btn_apri.clicked.connect(self.apri_cliente)
    def inserimento_nome(self):
        try:
            cliente = self.gestore_clienti.ricerca_cliente_codice_null(self.line_barra.text())
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
            QMessageBox.critical(self,'Errore','Il cliente ha già la tessera o è inisistente')
            print(m)
    def apri_cliente(self):
        try:
            selected = self.lista_clienti.selectedIndexes()[0].data()
            id = (selected.split('-')[0].strip().split(':')[1])
            print('id selezionato è: '+id)
            cliente_ricercato = self.gestore_clienti.ricerca_cliente(id)
            self.go_inserimento = InserimentoTessera(cliente_ricercato)
            self.go_inserimento.show()
            self.close()
        except Exception as m:
            print(m)