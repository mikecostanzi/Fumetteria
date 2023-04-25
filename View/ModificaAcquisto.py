from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from Controller.GestoreAcquisti import GestoreAcquisti


class ModificaAcquisto(QWidget):
    def __init__(self,codice):
        super(ModificaAcquisto,self).__init__()
        self.codice = codice
        uic.loadUi('../ui/modifica-acquisto.ui',self)
        self.btn_data.clicked.connect(self.conferma_data)
        self.btn_importo.clicked.connect(self.conferma_importo)
    def conferma_data(self):
        data = self.line_data.text()
        gestore_acquisti = GestoreAcquisti()
        gestore_acquisti.modfica_data(self.codice,data)
        print('Premuto conferma data')
    def conferma_importo(self):
        importo = self.line_importo.text()
        gestore_acquisti = GestoreAcquisti()
        gestore_acquisti.modfica_importo(self.codice,importo)
        print('Premuto conferma importo')