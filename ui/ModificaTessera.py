from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from Controller.GestoreTessere import GestoreTessere

class ModificaTessera(QWidget):

    def __init__(self, codice):
        super(ModificaTessera, self).__init__()
        self.codice = codice
        uic.loadUi('modificaTessera.ui', self)
        self.btn_conferma.clicked.connect(self.confermaPunti)

    def confermaPunti(self):
        punti = int(self.linePunti.text())
        modifica = GestoreTessere()
        modifica.modifica_punti(self.codice, punti)
        print('Premuto conferma')
