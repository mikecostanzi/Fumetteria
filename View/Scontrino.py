from PyQt6.QtWidgets import QWidget


class Scontrino(QWidget):
    def __init__(self,codice):
        super(Scontrino,self).__init__()
        self.codice = codice