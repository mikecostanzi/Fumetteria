from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget, QListView

from Controller.GestoreFumetti import GestoreFumetti
from Model.Fumetto import Fumetto
from ui.VistaFumetto import VistaFumetto


class RicercaFumetti(QWidget):
    def __init__(self):
        super(RicercaFumetti,self).__init__()
        uic.loadUi('ricerca-fumetti.ui',self)
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
                riga = f"Codice:{elemento[0]} - Categoria: {elemento[1]} - Editore: {elemento[3]} - Qtità: {elemento[7]}"
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
            print("ricerca di mockup non andato a buon fune")
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
            f = Fumetto(dato[0],dato[1],dato[2],dato[3],dato[4],dato[5],dato[6],dato[7])
            print(f.get_barcode())
            self.go_vista_fumetto = VistaFumetto(fumetto_ricercato)

            self.go_vista_fumetto.show()

        except Exception as m:
            print("errore nel try")
            print(m)