from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from Controller.GestoreFumetti import GestoreFumetti


class EliminaFumetto(QWidget):
    def __init__(self,barcode):
        super(EliminaFumetto,self).__init__()
        uic.loadUi('elimina-fumetto.ui',self)
        self.barcode = barcode
        self.btn_conferma.clicked.connect(self.elimina)
        self.btn_annulla.clicked.connect(self.close)
    def elimina(self):
        fumetto_eliminare = GestoreFumetti()
        fumetto_eliminare.elimina_fumetto(self.barcode)
        self.close()

