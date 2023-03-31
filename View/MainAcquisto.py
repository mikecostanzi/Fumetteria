from PyQt6 import uic
from PyQt6.QtWidgets import QWidget


class MainAcquisto(QWidget):
    def __init__(self):
        super(MainAcquisto,self).__init__()
        uic.loadUi('../ui/main-acquisto.ui',self)