from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget, QMessageBox

from Controller.GestoreAcquisti import GestoreAcquisti
from Controller.GestoreFumetti import GestoreFumetti
from View.Scontrino import Scontrino


class RicercaFumettiAcquistati(QWidget):
    def __init__(self,codice):
        super(RicercaFumettiAcquistati,self).__init__()
        uic.loadUi('../ui/ricerca-fumetti-acquistati.ui',self)
        self.codice = codice
        self.gestore_acquisti = GestoreAcquisti()
        self.btn_cerca.clicked.connect(self.inserimento_barcode)
        self.btn_inserisci.clicked.connect(self.inserimento_in_acquisto)
        self.btn_completa.clicked.connect(self.go_completa_acquisto)
    def inserimento_barcode(self):
        try:
            ricerca_fumetti = GestoreFumetti()
            fumetto = ricerca_fumetti.ricerca(self.line_barcode.text())
            lista_model = QStandardItemModel(self.lista_fumetti)
            for elemento in fumetto:
                item = QStandardItem()
                riga = f"Barcode:{elemento[0]} - Titolo: {elemento[1]} Categoria: {elemento[2]} - Editore: {elemento[4]} - Qtità: {elemento[8]}"
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
    def inserimento_in_acquisto(self):
        selected = self.lista_fumetti.selectedIndexes()[0].data()
        barcode = int(selected.split("-")[0].strip().split(":")[1])
        print(barcode)
        self.gestore_acquisti.inserisci_fumetti_acquistati(self.codice,barcode)
        print(f'Inserimento di {barcode} fatto')
    def go_completa_acquisto(self):
        self.gestore_acquisti.set_importo(self.codice)
        self.gestore_acquisti.set_punti(self.codice)
        self.go_scontrino = Scontrino(self.codice)
        self.go_scontrino.show()
        self.close()
