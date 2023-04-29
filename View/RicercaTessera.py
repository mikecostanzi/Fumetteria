from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget, QListView, QMessageBox

from Controller.GestoreTessere import GestoreTessere
from Model.Tessera import Tessera
from View.VistaTessera import VistaTessera


class RicercaTessera(QWidget):
    def __init__(self):
        super(RicercaTessera, self).__init__()
        uic.loadUi('../ui/ricercaTessera.ui', self)
        self.gestore_tessere = GestoreTessere()
        self.btn_ricerca.clicked.connect(self.inserimento_codice)
        self.btn_apri.clicked.connect(self.apri_tessera)

    def inserimento_codice(self):
        try:
            tessera = self.gestore_tessere.ricercaTessera(self.line_barra.text())
            lista_model = QStandardItemModel(self.listaTessere)

            for elemento in tessera:
                item = QStandardItem()
                riga = f'Codice:{elemento[0]} - Data Iscrizione: {elemento[1]} - Punti: {elemento[2]}'
                print(riga)
                item.setText(riga)
                item.setEditable(False)
                font = item.font()
                font.setPixelSize(18)
                item.setFont(font)
                lista_model.appendRow(item)
            self.listaTessere.setModel(lista_model)
        except Exception as m:
            QMessageBox.critical(self,'Errore','La tessera non esiste')
            print(m)
    def apri_tessera(self):
        try:
            selected = self.listaTessere.selectedIndexes()[0].data()
            codice = selected.split('-')[0].strip().split(':')[1]
            print('id selezionato è: '+codice)
            tessera_ricercata = self.gestore_tessere.ricercaTessera(codice)
            self.go_vista_tessera = VistaTessera(tessera_ricercata)
            self.go_vista_tessera.show()
        except Exception as m:
            print(m)
