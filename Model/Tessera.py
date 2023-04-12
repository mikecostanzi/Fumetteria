class Tessera:

    def __init__(self, codice,data_inizio, punti):
        self.codice = codice
        self.data_inizio = data_inizio
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
