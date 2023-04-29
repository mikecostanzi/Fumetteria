from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget, QMessageBox

from Controller.GestoreFumetti import GestoreFumetti
from Model.Fumetto import Fumetto
from View.VistaFumetto import VistaFumetto


class RicercaFumetti(QWidget):
    def __init__(self):
        super(RicercaFumetti,self).__init__()
        uic.loadUi('../ui/ricerca-fumetti.ui',self)
        self.gestore_fumetti = GestoreFumetti()
        self.btn_ricerca.clicked.connect(self.inserimento_codice)
        self.btn_apri.clicked.connect(self.apri_fumetto)

    def inserimento_codice(self):
        try:
            fumetto = self.gestore_fumetti.ricerca(self.line_barra.text())
            lista_model = QStandardItemModel(self.lista_fumetti)
            for elemento in fumetto:
                item = QStandardItem()
                riga = f"Codice:{elemento[0]} - Titolo: {elemento[1]} Categoria: {elemento[2]} - Editore: {elemento[4]} - Qtità: {elemento[8]}"
                print(riga)
                item.setText(riga)
                item.setEditable(False)
                font = item.font()
                font.setPixelSize(18)
                item.setFont(font)
                lista_model.appendRow(item)
            self.lista_fumetti.setModel(lista_model)
        except:
            QMessageBox.critical(self,'Errore','Il fumetto non esiste')
            print("Fumetto non esistente")
    def apri_fumetto(self):
        try:
            selected = self.lista_fumetti.selectedIndexes()[0].data()
            codice = int(selected.split("-")[0].strip().split(":")[1])
            print('Codice selezionato: '+ str(codice))
            fumetto_ricercato = self.gestore_fumetti.ricerca(codice)
            self.go_vista_fumetto = VistaFumetto(fumetto_ricercato)
            self.go_vista_fumetto.show()
        except Exception as m:
            print("Errore nel try di apri fumetto")
            print(m)