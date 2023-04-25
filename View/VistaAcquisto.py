from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget

from Controller.GestoreAcquisti import GestoreAcquisti
from Model.Acquisto import Acquisto
from View.EliminaAcquisto import EliminaAcquisto
from View.ModificaAcquisto import ModificaAcquisto


class VistaAcquisto(QWidget):
    def __init__(self,acquisto):
        super(VistaAcquisto,self).__init__()
        uic.loadUi('../ui/vista-acquisto.ui',self)

        for dato in acquisto:
            self.a = Acquisto(dato[0],dato[1],dato[2],dato[3])
        self.l_data.setText(f'Data di acquisto: {self.a.get_data_acquisto()}')
        self.l_importo.setText(f'Importo totale: {self.a.get_importo()}')
        self.l_punti.setText(f'Punti ottenuti: {self.a.get_punti()}')
        gestore_acquisti = GestoreAcquisti()
        fumetti_acquistati = gestore_acquisti.ricerca_fumetti_acquistati(self.a.get_codice())
        lista_model = QStandardItemModel(self.lista_fumetti)
        for elemento in fumetti_acquistati:
            item = QStandardItem()
            riga = f"Barcode:{elemento[0]}\nTitolo: {elemento[1]}\nCategoria: {elemento[2]}\nDistributore: {elemento[3]}\nEditore: {elemento[4]}\nPrezzo: {elemento[5]}\n"
            print(riga)
            item.setText(riga)
            item.setEditable(False)
            font = item.font()
            font.setPixelSize(18)
            item.setFont(font)
            lista_model.appendRow(item)
        self.lista_fumetti.setModel(lista_model)
        self.btn_modifica.clicked.connect(self.go_modifica)
        self.btn_elimina.clicked.connect(self.go_elimina)
        self.setWindowTitle(f'Acquisto codice: {self.a.get_codice()}')
    def go_modifica(self):
        self.modifica = ModificaAcquisto(self.a.get_codice())
        self.modifica.show()
        self.close()
    def go_elimina(self):
        self.elimina = EliminaAcquisto(self.a.get_codice())
        self.elimina.show()
        self.close()