from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from View.InserimentoCodiceAcquisto import InserimentoCodiceAcquisto


class MainAcquisto(QWidget):
    def __init__(self):
        super(MainAcquisto,self).__init__()
        uic.loadUi('../ui/main-acquisto.ui',self)
        self.btn_nuovo.clicked.connect(self.go_inserimento_acquisto)
    def go_inserimento_acquisto(self):
        self.go_inserimento = InserimentoCodiceAcquisto()
        self.go_inserimento.show()