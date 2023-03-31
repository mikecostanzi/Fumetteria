from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from Controller.GestoreTessere import GestoreTessere

class EliminaTessera(QWidget):
    def __init__(self, codice):
        super(EliminaTessera, self).__init__()
        uic.loadUi('../ui/eliminaTessera.ui', self)
        self.codice = codice
        self.btn_conferma.clicked.connect(self.elimina)
        self.btn_annulla.clicked.connect(self.close)

    def elimina(self):
        tessera_eliminare = GestoreTessere()
        tessera_eliminare.eliminaFumetto(self.codice)
        self.close()