from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from ui.RicercaTessera import RicercaTessera
from ui.InserimentoTessera import InserimentoTessera

class MainTessera(QWidget):

    def __init__(self):
        super(MainTessera, self).__init__()
        uic.loadUi('MainTessera.ui', self)
        self.btn_inserisci.clicked.connect(self.go_inserisci)
        self.btn_ricerca.clicked.connect(self.go_ricerca)
        self.show()

    def go_inserisci(self):
        self.inserimento_tessera = InserimentoTessera()
        self.inserimento_tessera.show()

    def go_ricerca(self):
        self.ricerca = RicercaTessera()
        self.ricerca.show()