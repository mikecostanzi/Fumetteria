from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget

from Sistema.GestoreStatistiche import GestoreStatistiche


class Statistiche(QWidget):
    def __init__(self):
        super(Statistiche,self).__init__()
        self.gestore_statistiche = GestoreStatistiche()
        prima = self.gestore_statistiche.prima_statistica()
        terza = self.gestore_statistiche.terza_statistica()
        quarta = self.gestore_statistiche.quarta_statistica()
        uic.loadUi('../ui/statistiche.ui',self)
        self.l_prima.setText(f'Il totale dei clienti tesserati è: {prima}')
        self.l_terza.setText(f'Il numero dei fumetti venduti della Dc è: {terza}')
        self.l_quarta.setText(f'Il numero dei fumetti venduti della Marvel è: {quarta}')
        self.btn_conferma.clicked.connect(self.inserimento_data)
    def inserimento_data(self):
        seconda = self.gestore_statistiche.seconda_statistica(self.line_data.text())
        lista_model = QStandardItemModel(self.lista_importo)
        for i in seconda:
            item = QStandardItem()
            riga = f'{i[0]} euro'
            item.setText(riga)
            item.setEditable(False)
            font = item.font()
            font.setPixelSize(18)
            item.setFont(font)
            lista_model.appendRow(item)
        self.lista_importo.setModel(lista_model)


