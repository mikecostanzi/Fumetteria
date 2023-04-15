class Tessera:

    def __init__(self, codice,data_inizio, punti):
        self.codice = codice
        self.data_inizio = data_inizio
        self.punti = punti

    def getCodice(self):
        return self.codice

    def getDataInizio(self):
        return self.data_inizio

    def getPunti(self):
        return self.punti
