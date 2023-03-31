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
        self.lista = []
        self.btn_ricerca.clicked.connect(self.inserimento_codice)
        self.btn_apri.clicked.connect(self.apri_fumetto)

    def inserimento_codice(self):
        print('--- Inizio barra di ricerca ---')
        try:
            ricerca_fumetti = GestoreFumetti()
            fumetto = ricerca_fumetti.ricerca(self.line_barra.text())

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
            print(self.lista)
        except:
            QMessageBox.critical(self,'Errore','Il fumetto non esiste')
            print("Fumetto non esistente")
    def apri_fumetto(self):
        print("--- Inizio metodo apri_fumetto ---")
        try:
            selected = self.lista_fumetti.selectedIndexes()[0].data()
            codice = int(selected.split("-")[0].strip().split(":")[1])
            print(codice)
            fumetto = GestoreFumetti()
            fumetto_ricercato = fumetto.ricerca(codice)
            i = 0
            for dato in fumetto_ricercato:
                print(dato[i])
                i += 1
            f = Fumetto(dato[0],dato[1],dato[2],dato[3],dato[4],dato[5],dato[6],dato[7],dato[8])
            print(f.get_barcode())
            self.go_vista_fumetto = VistaFumetto(fumetto_ricercato)

            self.go_vista_fumetto.show()
            print('--- Fiine metodo apri fumetto ---')

        except Exception as m:
            print("Errore nel try di apri fumetto")
            print(m)