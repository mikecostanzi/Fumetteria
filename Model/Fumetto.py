class Fumetto:
    def __init__(self):
        self.barcode = -3
        self.categoria = " "
        self.distributore = " "
        self.editore = " "
        self.collana = -1
        self.sottocollana = -2
        self.quantita = 0
        self.prezzo = -1.01


    def getFumetto(self):
        return {
            "barcode": self.barcode,
            "categoria": self.categoria,
            "distributore": self.distributore,
            "editore": self.editore,
            "collana": self.collana,
            "sottocollana": self.sottocollana,
            "quantita": self.quantita,
            "prezzo": self.prezzo,

        }