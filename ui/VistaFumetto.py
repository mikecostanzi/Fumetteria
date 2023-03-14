from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QLabel

from Model.Fumetto import Fumetto


class VistaFumetto(QWidget):
    def __init__(self,fumetto):
        super(VistaFumetto,self).__init__()
        print('--- Inizio costruttore VistaFumetto ---')
        print(fumetto)
        uic.loadUi("vista-fumetto.ui",self)

        for dato in fumetto:
            f = Fumetto(dato[0],dato[1],dato[2],dato[3],dato[4],dato[5],dato[6],dato[7])

        self.l_categoria.setText(f'Categoria: {f.get_categoria()}')
        self.l_distributore.setText(f'Distributore: {f.get_distributore()}')
        self.l_editore.setText(f'Editore: {f.get_editore()}')
        self.l_collana.setText(f'Collana: {f.get_collana()}')
        self.l_sottocollana.setText(f'Sottocollana: {f.get_sottocollana()}')
        self.l_prezzo.setText(f'Prezzo: {f.get_prezzo()}')
        self.l_quantita.setText(f'Quantità: {f.get_quantita()}')
        self.setWindowTitle(f'Fumetto: {f.get_barcode()}')
