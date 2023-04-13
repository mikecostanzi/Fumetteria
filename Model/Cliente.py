
class Cliente:
    def __init__(self,id,nome,cognome,indirizzo,telefono,email,codice):
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.indirizzo = indirizzo
        self.telefono = telefono
        self.email = email
        self.codice = codice

    def get_id(self):
        return self.id
    def get_nome(self):
        return self.nome
    def get_cognome(self):
        return self.cognome
    def get_indirizzo(self):
        return self.indirizzo
    def get_telefono(self):
        return self.telefono
    def get_email(self):
        return self.email
    def get_codice(self):
        return self.codice