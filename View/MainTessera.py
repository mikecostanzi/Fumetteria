from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from View.RicercaClienteTessera import RicercaClienteTessera
from View.RicercaTessera import RicercaTessera
from View.InserimentoTessera import InserimentoTessera

class MainTessera(QWidget):

    def __init__(self):
        super(MainTessera, self).__init__()
        uic.loadUi('../ui/MainTessera.ui', self)
        self.btn_inserisci.clicked.connect(self.go_inserisci)
        self.btn_ricerca.clicked.connect(self.go_ricerca)
        self.show()

    def go_inserisci(self):
        self.inserimento_tessera = RicercaClienteTessera()
        self.inserimento_tessera.show()

    def go_ricerca(self):
        self.ricerca = RicercaTessera()
        self.ricerca.show()