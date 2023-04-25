from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from Controller.GestoreAcquisti import GestoreAcquisti


class EliminaAcquisto(QWidget):
    def __init__(self,codice):
        super(EliminaAcquisto,self).__init__()
        self.codice = codice
        self.gestore_acquisti = GestoreAcquisti()
        uic.loadUi('../ui/elimina-acquisto.ui',self)
        self.btn_conferma.clicked.connect(self.elimina)
        self.btn_annulla.clicked.connect(self.close)
    def elimina(self):
        self.gestore_acquisti.elimina_acquisto(self.codice)
        self.close()
        print('Acquisto eliminato')
