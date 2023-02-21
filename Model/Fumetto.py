class Fumetto:
    def __init__(self,barcode,categoria,distributore,editore,collana,sottocollana,prezzo,quantita):
        self.barcode = barcode
        self.categoria = categoria
        self.distributore = distributore
        self.editore = editore
        self.collana = collana
        self.sottocollana = sottocollana
        self.prezzo = prezzo
        self.quantita = quantita
    def get_barcode(self):
        return self.barcode
    def get_categoria(self):
        return self.categoria
    def get_distributore(self):
        return self.distributore
    def get_editore(self):
        return self.editore
    def get_collana(self):
        return self.collana
    def get_sottocollana(self):
        return self.sottocollana
    def get_prezzo(self):
        return self.prezzo
    def get_quantita(self):
        return self.quantita