from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow

from Sistema.GestoreBackup import GestoreBackup
from View.MainAcquisto import MainAcquisto
from View.MainCliente import MainCliente
from View.MainTessera import MainTessera
from View.MainMagazzino import MainMagazzino
from View.Statistiche import Statistiche


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi("../ui/inizio.ui", self)
        self.btn_acquisto.clicked.connect(self.go_acquisto)
        self.btn_cliente.clicked.connect(self.go_tessera)
        self.btn_magazzino.clicked.connect(self.go_magazzino)
        self.btn_backup.clicked.connect(self.go_backup)
        self.btn_statistche.clicked.connect(self.go_statistiche)

        self.show()
    def go_acquisto(self):
        self.main_acquisto = MainAcquisto()
        self.main_acquisto.show()

    def go_tessera(self):
        self.main_cliente=MainCliente()
        self.main_cliente.show()

    def go_magazzino(self):
        self.main_magazzino = MainMagazzino()
        self.main_magazzino.show()
    def go_backup(self):
        backup = GestoreBackup()
        backup.b_fumetti()
        backup.b_clienti()
        backup.b_tessere()
        backup.b_acquisti()

    def go_statistiche(self):
        self.statitstiche = Statistiche()
        self.statitstiche.show()