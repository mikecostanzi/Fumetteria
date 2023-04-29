from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from Model.Tessera import Tessera
from View.EliminaTessera import EliminaTessera
from View.ModificaTessera import ModificaTessera

class VistaTessera(QWidget):
    def __init__(self, tessera):
        super(VistaTessera, self).__init__()
        uic.loadUi("../ui/vistaTessera.ui", self)

        for dato in tessera:
            t = Tessera(dato[0], dato[1], dato[2])
            self.tessera_da_eliminare = Tessera(dato[0], dato[1], dato[2])
            self.tessera_da_modificare = Tessera(dato[0], dato[1], dato[2])

        self.labelCodice.setText(f'Codice: {t.getCodice()}')
        self.labelData.setText(f'DataNascita: {t.getDataInizio()}')
        self.labelPunti.setText(f'Punti: {t.getPunti()}')
        self.btn_modifica.clicked.connect(self.goModifica)
        self.btn_elimina.clicked.connect(self.goElimina)

    def goElimina(self):
        self.get_eliminazione = EliminaTessera(self.tessera_da_eliminare.getCodice())
        self.get_eliminazione.show()
        self.close()

    def goModifica(self):
        self.get_modifica = ModificaTessera(self.tessera_da_modificare.getCodice())
        self.get_modifica.show()
        self.close()
