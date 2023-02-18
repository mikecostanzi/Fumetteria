from PyQt6.QtWidgets import QWidget, QDialog, QLabel
from PyQt6 import uic

import sys
class VistaOperazioniFumetti(QDialog):
    def __int__(self,parent=None):
        super(VistaOperazioniFumetti,self).__int__(parent)
        uic.loadUi("ui/vista_operazioni_fumetti.ui")
        self.label = QLabel("ciao")

        


    def go_inserisci(self):
        pass
    def go_cerca(self):
        pass

