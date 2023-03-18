class Tessera:

    def __init__(self, codice, nome, cognome, dataNascita, punti):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome
        self.dataNascita = dataNascita
        self.punti = punti

    def getCodice(self):
        return self.codice

    def getNome(self):
        return self.nome

    def getCognome(self):
        return self.cognome

    def getDataNascita(self):
        return self.dataNascita

    def getPunti(self):
        return self.punti
