from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget, QListView, QMessageBox

from Controller.GestoreTessere import GestoreTessere
from Model.Tessera import Tessera

class RicercaTessera(QWidget):
    def __init__(self):
        super(RicercaTessera, self).__init__()
        uic.loadUi('../ui/ricercaTessera.ui', self)
        self.lista = []
        self.btn_ricerca.clicked.connect(self.inserimentoCodice)
        self.btn_apri.clicked.connect(self.apriFumetto)