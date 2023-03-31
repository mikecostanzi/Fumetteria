from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from Model.Tessera import Tessera
from View.EliminaTessera import EliminaTessera
from View.ModificaTessera import ModificaTessera

class VistaTessera(QWidget):
    def __init__(self, tessera):
        super(VistaTessera, self).__init__()
        print('--- Inizio costruttore VistaTessera ---')
        print(tessera)
        uic.loadUi("../ui/vistaTessera.ui", self)

        for dato in tessera:
            t = Tessera(dato[0], dato[1], dato[2], dato[3], dato[4])
            self.tessera_da_eliminare = Tessera(dato[0], dato[1], dato[2], dato[3], dato[4])
            self.tessera_da_modificare = Tessera(dato[0], dato[1], dato[2], dato[3], dato[4])

        self.labelCodice.setText(f'Codice: {t.getCodice()}')
        self.labelNome.setText(f'Nome: {t.getNome()}')
        self.labelCognome.setText(f'Cognome: {t.getCognome()}')
        self.labelData.setText(f'DataNascita: {t.getDataNascita()}')
        self.labelPunti.setText(f'Punti: {t.getPunti()}')
        self.btn_modiifca.clicked.connect(self.goModifica)
        self.btn_elimina.clicked.connect(self.goElimina)

    def goElimina(self):
        self.get_eliminazione = EliminaTessera(self.tessera_da_eliminare.getCodice())
        self.get_eliminazione.show()
        self.close()

    def goModifica(self):
        self.get_modifica = ModificaTessera(self.tessera_da_modificare.getCodice())
        self.get_modifica.show()
        self.close()