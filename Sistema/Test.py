import unittest

from Controller.GestoreClienti import GestoreClienti
from Controller.GestoreFumetti import GestoreFumetti
from Model.Cliente import Cliente
from Model.Fumetto import Fumetto
class Test(unittest.TestCase):
    def test_controllo_fumetto(self):
        barcode = 99
        titolo = 'Titolo'
        categoria = 'Categoria'
        distributore = 'Distributore'
        editore = 'Editore'
        collana = 99
        sottocollana = 99
        prezzo = 1.5
        quantita = 1
        fumetto = Fumetto(barcode, titolo, categoria, distributore, editore, collana, sottocollana, prezzo, quantita)
        gestore = GestoreFumetti()
        gestore.elimina_fumetto(barcode)
        gestore.inserisci_fumetto(barcode,titolo,categoria,distributore,editore,collana,sottocollana,prezzo,quantita)
        f = gestore.ricerca(barcode)
        for dato in f:
            fumetto_ricercato = Fumetto(dato[0],dato[1],dato[2],dato[3],dato[4],dato[5],dato[6],dato[7],dato[8])
        try:

            self.assertEqual(fumetto,fumetto_ricercato)
        except Exception as m:
            print(m)
    def test_controllo_cliente(self):
        id = 99
        nome = 'nome'
        cognome = 'cognome'
        indirizzo = 'indirizzo'
        telefono = '12345678'
        email = 'email'
        codice = None
        cliente = Cliente(id,nome,cognome,indirizzo,telefono,email,codice)
        gestore = GestoreClienti()
        gestore.elimina_cliente(id)
        gestore.inserisci_cliente(id,nome,cognome,indirizzo,telefono,email,codice)
        c = gestore.ricerca_cliente(id)
        for dato in c:
            cliente_ricercato = Cliente(dato[0],dato[1],dato[2],dato[3],dato[4],dato[5],dato[6])
        try:
            self.assertTrue(cliente==cliente_ricercato)
            self.assertEqual(cliente,cliente_ricercato)
        except Exception as m:
            print(m)

if __name__ == '__main__':
    unittest.main()


