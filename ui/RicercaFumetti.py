from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget

from Controller.GestoreFumetti import GestoreFumetti


class RicercaFumetti(QWidget):
    def __init__(self):
        super(RicercaFumetti,self).__init__()
        uic.loadUi('ricerca-fumetti.ui',self)
        self.lista = []
        self.btn_ricerca.clicked.connect(self.inserimento_codice)

    def inserimento_codice(self):
        try:
            ricerca_fumetti = GestoreFumetti()
            fumetto = ricerca_fumetti.ricerca(self.line_barra.text())

            lista_model = QStandardItemModel(self.lista_fumetti)
            for elemento in fumetto:
                item = QStandardItem()
                riga = f"Codice:{elemento[0]} - Categoria: {elemento[1]} - Editore: {elemento[3]} - Qtità: {elemento[7]}"
                item.setText(riga)
                item.setEditable(False)
                font = item.font()
                font.setPixelSize(18)
                item.setFont(font)
                lista_model.appendRow(item)
            self.lista_fumetti.setModel(lista_model)
            print(self.lista)



        except:
            print("ricerca di mockup non andato a buon fune")