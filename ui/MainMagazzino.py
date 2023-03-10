from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from Controller.GestoreFumetti import GestoreFumetti
from ui.InserimentoFumetto import InserimentoFumetto
from ui.RicercaFumetti import RicercaFumetti


class MainMagazzino(QWidget):
    
    def __init__(self):
        super(MainMagazzino,self).__init__()
        uic.loadUi('main-magazzino.ui',self)
        self.btn_inserisci.clicked.connect(self.go_inserisci)
        self.btn_ricerca.clicked.connect(self.go_ricerca)

        self.show()
    def go_inserisci(self):
        self.inserimento_fumetto = InserimentoFumetto()
        self.inserimento_fumetto.show()

    def go_ricerca(self):
        self.ricerca = RicercaFumetti()
        self.ricerca.show()
