from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget, QMessageBox

from Controller.GestoreAcquisti import GestoreAcquisti
from Model.Acquisto import Acquisto
from View.RicercaTessera import RicercaTessera


class Scontrino(QWidget):
    def __init__(self,codice):
        super(Scontrino,self).__init__()
        self.codice = codice
        uic.loadUi('../ui/scontrino.ui',self)
        gestore_acquisti = GestoreAcquisti()
        acquisto = gestore_acquisti.ricerca_acquisto(self.codice)
        fumetti_acquistati = gestore_acquisti.ricerca_fumetti_acquistati(self.codice)
        for dato in acquisto:
            self.a = Acquisto(dato[0],dato[1],dato[2],dato[3])

        self.l_data.setText(f'Data di acquisto: {self.a.get_data_acquisto()}')
        self.l_importo.setText(f'Importo totale: {self.a.get_importo()}')
        self.l_punti.setText(f'Punti acquisiti: {self.a.get_punti()}')
        lista_model = QStandardItemModel(self.lista_fumetti)
        for elemento in fumetti_acquistati:
            item = QStandardItem()
            riga = f"Barcode:{elemento[0]}\nTitolo: {elemento[1]}\nCategoria: {elemento[2]}\nDistributore: {elemento[3]}\nEditore: {elemento[4]}\nPrezzo: {elemento[5]}\n"
            print(riga)
            item.setText(riga)
            item.setEditable(False)
            font = item.font()
            font.setPixelSize(18)
            item.setFont(font)
            lista_model.appendRow(item)
        self.lista_fumetti.setModel(lista_model)

        self.btn_conferma.clicked.connect(self.close)
        self.btn_tessera.clicked.connect(self.go_ricerca_tessera)

        self.setWindowTitle(f'Scontrino - Codice: {self.a.get_codice()}')
    def go_ricerca_tessera(self):
        self.ricerca_tessera = RicercaTessera()
        self.ricerca_tessera.show()
        self.close()
        QMessageBox.critical(self,'Attenzione',f'Ricordati di aumentare di {self.a.get_punti()} punti al cliente')