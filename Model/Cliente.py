import datetime


class Cliente:
    def __init__(self):
        self.idCliente = -1
        self.nome = " "
        self.cognome = ""
        self.dataNascita = datetime.datetime(day=1, month=1, year=1922)
        self.indirizzo = ""
        self.telefono = ""
        self.email = ""

    def getCliente(self):
        return {
            "idCliente": self.idCliente,
            "cognome": self.cognome,
            "nome": self.nome,
            "dataNascita": self.dataNascita,
            "indirizzo": self.indirizzo,
            "telefono": self.telefono,
            "email": self.email,
        }

