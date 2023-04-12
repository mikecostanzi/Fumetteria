from PyQt6 import uic
from PyQt6.QtWidgets import QWidget


class InserimentoCliente(QWidget):

    def __init__(self):
        super(InserimentoCliente,self).__init__()
        uic.loadUi('../ui/inserimento-cliente.ui',self)

