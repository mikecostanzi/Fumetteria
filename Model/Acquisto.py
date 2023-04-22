

class Acquisto:
    def __init__(self,codice,data_acquisto,importo_totale,punti):
        self.codice = codice
        self.data_acquisto = data_acquisto
        self.importo_totale = importo_totale
        self.punti = punti

    def get_codice(self):
        return self.codice
    def get_data_acquisto(self):
        return self.data_acquisto
    def get_importo(self):
        return self.importo_totale
    def get_punti(self):
        return self.punti
