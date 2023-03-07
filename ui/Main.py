from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow


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
        pass

    def go_magazzino(self):
        self.main_magazzino = MainMagazzino()
        self.main_magazzino.show()
    def go_backup(self):
        pass
    def go_statistiche(self):
        pass