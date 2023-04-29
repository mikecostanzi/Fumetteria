from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from Model.Fumetto import Fumetto
from View.EliminaFumetto import EliminaFumetto
from View.ModificaFumetto import ModificaFumetto


class VistaFumetto(QWidget):
    def __init__(self,fumetto):
        super(VistaFumetto,self).__init__()
        uic.loadUi("../ui/vista-fumetto.ui",self)
        for dato in fumetto:
            f = Fumetto(dato[0],dato[1],dato[2],dato[3],dato[4],dato[5],dato[6],dato[7],dato[8])
            self.fumetto_da_eliminare = Fumetto(dato[0],dato[1],dato[2],dato[3],dato[4],dato[5],dato[6],dato[7],dato[8])
            self.fumetto_da_modificare = Fumetto(dato[0],dato[1],dato[2],dato[3],dato[4],dato[5],dato[6],dato[7],dato[8])

        self.l_titolo.setText(f'Titolo: {f.get_titolo()}')
        self.l_categoria.setText(f'Categoria: {f.get_categoria()}')
        self.l_distributore.setText(f'Distributore: {f.get_distributore()}')
        self.l_editore.setText(f'Editore: {f.get_editore()}')
        self.l_collana.setText(f'Collana: {f.get_collana()}')
        self.l_sottocollana.setText(f'Sottocollana: {f.get_sottocollana()}')
        self.l_prezzo.setText(f'Prezzo: {f.get_prezzo()}')
        self.l_quantita.setText(f'Quantità: {f.get_quantita()}')
        self.setWindowTitle(f'Fumetto: {f.get_barcode()}')
        self.btn_modifica.clicked.connect(self.go_modifica)
        self.btn_elimina.clicked.connect(self.go_eliminazione)


    def go_eliminazione(self):
        self.get_eliminazione = EliminaFumetto(self.fumetto_da_eliminare.get_barcode())
        self.get_eliminazione.show()
        self.close()

    def go_modifica(self):
        self.get_modifica = ModificaFumetto(self.fumetto_da_modificare.get_barcode())
        self.get_modifica.show()
        self.close()

