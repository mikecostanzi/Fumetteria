from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from View.InserimentoCodiceAcquisto import InserimentoCodiceAcquisto
from View.RicercaAcquisti import RicercaAcquisti


class MainAcquisto(QWidget):
    def __init__(self):
        super(MainAcquisto,self).__init__()
        uic.loadUi('../ui/main-acquisto.ui',self)
        self.btn_nuovo.clicked.connect(self.go_inserimento_acquisto)
        self.btn_ricerca.clicked.connect(self.go_ricerca)
    def go_inserimento_acquisto(self):
        self.go_inserimento = InserimentoCodiceAcquisto()
        self.go_inserimento.show()
    def go_ricerca(self):
        self.ricerca_acquisti = RicercaAcquisti()
        self.ricerca_acquisti.show()