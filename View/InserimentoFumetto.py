from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox

from Controller.GestoreFumetti import GestoreFumetti


class InserimentoFumetto(QWidget):
    def __init__(self):
        super(InserimentoFumetto,self).__init__()
        uic.loadUi('../ui/inserimento-fumetto.ui',self)
        self.btn_inserisci.clicked.connect(self.inserimento)

        self.show()

    def inserimento(self):
        barcode = int(self.line_barcode.text())
        titolo = self.line_titolo.text()
        categoria = self.line_categoria.text()
        distributore = self.line_distributore.text()
        editore = self.line_editore.text()
        collana = int(self.line_collana.text())
        sottocollana = int(self.line_sottocollana.text())
        prezzo = float(self.line_prezzo.text())
        quantita = int(self.line_quantita.text())

        fumetto = GestoreFumetti()

        if (not barcode) or (not prezzo) or (not quantita):
            QMessageBox.critical(self,'Errore', 'Inserisci i dati necessari')
        else:
            fumetto.inserisci_fumetto(barcode,titolo,categoria,distributore,editore,collana,sottocollana,prezzo,quantita)
            QMessageBox.critical(self,'Successo!','Inserimento corretto')
            self.close()


