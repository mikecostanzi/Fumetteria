from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow

from ui.MainTessera import MainTessera
from ui.MainMagazzino import MainMagazzino


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi("inizio.ui", self)
        self.btn_acquisto.clicked.connect(self.go_acquisto)
        self.btn_cliente.clicked.connect(self.go_tessera)
        self.btn_magazzino.clicked.connect(self.go_magazzino)

        self.show()
    def go_acquisto(self):
        pass
    def go_tessera(self):
        self.main_tessera = MainTessera()
        self.main_tessera.show()

    def go_magazzino(self):
        self.main_magazzino = MainMagazzino()
        self.main_magazzino.show()
    def go_backup(self):
        pass
    def go_statistiche(self):
        pass