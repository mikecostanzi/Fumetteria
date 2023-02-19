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

    def get_idCliente(self):
        return self.idCliente
    def get_nome(self):
        return self.nome
    def get_cognome(self):
        return self.cognome
    def get_dataNascita(self):
        return self.dataNascita
    def get_indirizzo(self):
        return self.indirizzo
    def get_telefono(self):
        return self.telefono
    def get_email(self):
        return self.email

