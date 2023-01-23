from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLabel, QDialog

#from ui.VistaOperazioniFumetti import Ui_VistaOperazioniFumetti
from View.VistaOperazioniFumetti import VistaOperazioniFumetti

class InterfacciaMain(QDialog):

    def __init__(self, parent=None):
        super(InterfacciaMain, self).__init__(parent)
        l = QGridLayout()
        b = QLabel()
        b.setText("Scegli l'operazione:")
        l.addWidget(b)
        l.addWidget(self.get_generic_button("Cliente", self.go_cliente), 1, 0)
        l.addWidget(self.get_generic_button("Magazzino", self.go_magazzino), 1, 1)
        l.addWidget(self.get_generic_button("Acquisto", self.go_acquisto), 1, 2)
        l.addWidget(self.get_generic_button("Buckup", self.go_buckup), 2, 1)
        l.addWidget(self.get_generic_button("Statistiche", self.go_statistiche), 2,2)
        self.setLayout(l)
        self.resize(500, 500)
        self.setWindowTitle("Main")

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button
    def go_cliente(self):
        pass
    def go_magazzino(self):
        self.vista_operazioni_fumetti = VistaOperazioniFumetti()
        self.vista_operazioni_fumetti.show()


    def go_acquisto(self):
        pass
    def go_buckup(self):
        pass
    def go_statistiche(self):
        pass