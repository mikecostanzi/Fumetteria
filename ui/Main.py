from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow

from ui.MainCliente import MainCliente
from ui.MainMagazzino import MainMagazzino


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi("inizio.ui", self)
        self.btn_acquisto.clicked.connect(self.go_acquisto)
        self.btn_cliente.clicked.connect(self.go_cliente)
        self.btn_magazzino.clicked.connect(self.go_magazzino)

        self.show()
    def go_acquisto(self):
        pass
    def go_cliente(self):
        self.main_cliente = MainCliente()
        self.main_cliente.show()
        self.close()

    def go_magazzino(self):
        self.main_magazzino = MainMagazzino()
        self.main_magazzino.show()
        self.close()

    def go_backup(self):
        pass
    def go_statistiche(self):
        pass