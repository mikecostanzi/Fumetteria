from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from Controller.GestoreFumetti import GestoreFumetti


class ModificaFumetto(QWidget):

    def __init__(self,barcode):
        super(ModificaFumetto,self).__init__()
        self.barcode = barcode
        uic.loadUi('../ui/modifica-fumetto.ui',self)
        self.btn_quantita.clicked.connect(self.conferma_quantita)

    def conferma_quantita(self):
        quantita = int(self.line_quantita.text())
        gestore = GestoreFumetti()
        gestore.modifica_quantita(self.barcode,quantita)
        print('Premuto conferma')