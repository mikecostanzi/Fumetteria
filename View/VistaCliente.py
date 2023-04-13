from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from Model.Cliente import Cliente
from View.EliminaCliente import EliminaCliente
from View.ModificaCliente import ModificaCliente


class VistaCliente(QWidget):
    def __init__(self,cliente):
        super(VistaCliente,self).__init__()
        uic.loadUi('../ui/vista-cliente.ui',self)
        for dato in cliente:
            self.c = Cliente(dato[0],dato[1],dato[2],dato[3],dato[4],dato[5],dato[6])

        self.l_nome.setText(f'Nome: {self.c.get_nome()}')
        self.l_cognome.setText(f'Cognome: {self.c.get_cognome()}')
        self.l_indirizzo.setText(f'Indirizzo: {self.c.get_indirizzo()}')
        self.l_telefono.setText(f'Telefono: {self.c.get_nome()}')
        self.l_email.setText(f'Email: {self.c.get_email()}')
        self.l_codice.setText(f'Codice della tessera: {self.c.get_codice()}')

        self.btn_elimina.clicked.connect(self.go_elimina)
        self.btn_modifica.clicked.connect(self.go_modifica)
        self.setWindowTitle(f'Cliente ID: {self.c.get_id()}' )

    def go_elimina(self):
        self.elimina = EliminaCliente(self.c.get_id())
        self.elimina.show()
        self.close()
    def go_modifica(self):
        self.modifica = ModificaCliente(self.c.get_id())
        self.modifica.show()
        self.close()