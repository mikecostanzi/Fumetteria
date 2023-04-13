from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from Controller.GestoreClienti import GestoreClienti


class EliminaCliente(QWidget):
    def __init__(self,id):
        super(EliminaCliente,self).__init__()
        self.id = id
        uic.loadUi('../ui/elimina-cliente.ui',self)
        self.btn_elimina.clicked.connect(self.elimina)
        self.btn_annulla.clicked.connect(self.close)
        self.setWindowTitle(f'ID Cliente da eliminare: {self.id}' )

    def elimina(self):
        self.gestore = GestoreClienti()
        self.eliminazione = self.gestore.elimina_cliente(self.id)
        print('Cliente eliminato con successo')
        self.close()