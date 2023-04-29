from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from Controller.GestoreFumetti import GestoreFumetti


class EliminaFumetto(QWidget):
    def __init__(self,barcode):
        super(EliminaFumetto,self).__init__()
        uic.loadUi('../ui/elimina-fumetto.ui',self)
        self.barcode = barcode
        self.btn_conferma.clicked.connect(self.elimina)
        self.btn_annulla.clicked.connect(self.close)
    def elimina(self):
        gestore_fumetti = GestoreFumetti()
        gestore_fumetti.elimina_fumetto(self.barcode)
        self.close()

