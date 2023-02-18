import datetime


class Cliente:
    def __init__(self,idCliente,nome,cognome,dataNascita,indirizzo,telefono,email):
        self.idCliente = idCliente
        self.nome = nome
        self.cognome = cognome
        self.dataNascita = dataNascita
        self.indirizzo = indirizzo
        self.telefono = telefono
        self.email = email


