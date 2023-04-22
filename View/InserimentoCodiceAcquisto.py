from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox

from Controller.GestoreAcquisti import GestoreAcquisti
from View.RicercaFumettiAcquistati import RicercaFumettiAcquistati


class InserimentoCodiceAcquisto(QWidget):

    def __init__(self):
        super(InserimentoCodiceAcquisto,self).__init__()
        uic.loadUi('../ui/inserimento-codice-acquisto.ui',self)
        self.btn_inserisci.clicked.connect(self.inserimento_codice)
    def inserimento_codice(self):
        try:
            codice = int(self.line_codice.text())
            data = self.line_data.text()
            gestore_acquisto = GestoreAcquisti()
            if not codice:
                QMessageBox.critical(self,'Errore','Inserisci i dati necessari')
            else:
                gestore_acquisto.nuovo_acquisto(codice,data)
                self.go_ricerca = RicercaFumettiAcquistati(codice)
                self.go_ricerca.show()
                self.close()
        except Exception as m:
            print(m)