from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox

from Controller.GestoreTessere import GestoreTessere

class InserimentoTessera(QWidget):
    def __init__(self):
        super(InserimentoTessera, self).__init__()
        uic.loadUi('InserimentoTessera.ui', self)
        self.btn_inserisci.clicked.connect(self.inserimento)
        self.show()

    def inserimento(self):
        nome = self.lineNome.text()
        cognome = self.lineCognome.text()
        dataNascita = self.lineData.text()
        punti = self.linePunti.text()

        tessera = GestoreTessere()

        if (not nome) or (not cognome) or (not dataNascita) or (not punti):
            QMessageBox.critical(self, 'Errore', 'Inserisci i dati mancanti')
        else:
            tessera.inserisciTessera(nome, cognome, dataNascita, punti)
            QMessageBox.text(self, 'Successo', 'Inserimento corretto')
            self.close()