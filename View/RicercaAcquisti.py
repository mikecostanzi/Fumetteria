from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget, QMessageBox

from Controller.GestoreAcquisti import GestoreAcquisti
from View.VistaAcquisto import VistaAcquisto


class RicercaAcquisti(QWidget):
    def __init__(self):
        super(RicercaAcquisti,self).__init__()
        uic.loadUi('../ui/ricerca-acquisti.ui',self)
        self.btn_cerca.clicked.connect(self.inserimento_codice)
        self.btn_apri.clicked.connect(self.apri_acquisto)
    def inserimento_codice(self):
        try:
            gestore_acquisti = GestoreAcquisti()
            acquisto = gestore_acquisti.ricerca_acquisto(self.line_codice.text())
            lista_model = QStandardItemModel(self.lista_acquisti)
            for elemento in acquisto:
                item = QStandardItem()
                riga = f"Codice:{elemento[0]}\nData acquisto: {elemento[1]}\nImporto totale: {elemento[2]}\nPunti: {elemento[3]} "
                print(riga)
                item.setText(riga)
                item.setEditable(False)
                font = item.font()
                font.setPixelSize(18)
                item.setFont(font)
                lista_model.appendRow(item)
            self.lista_acquisti.setModel(lista_model)
        except:
            QMessageBox.critical(self,'Errore','Acquisto inesistente')

    def apri_acquisto(self):
        selected = self.lista_acquisti.selectedIndexes()[0].data()
        codice = int(selected.split("\n")[0].strip().split(":")[1])
        print(codice)
        gestore_acquisti = GestoreAcquisti()
        acquisto_ricercato = gestore_acquisti.ricerca_acquisto(codice)
        print('acquisto ricercato: ' + str(acquisto_ricercato))
        self.vista_acquisto = VistaAcquisto(acquisto_ricercato)
        self.vista_acquisto.show()


