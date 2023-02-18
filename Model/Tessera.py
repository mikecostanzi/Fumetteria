from Model.Cliente import Cliente


class Tessera(Cliente):
    def __init__(self,n_punti):
        super(Cliente,self).__init__()
        self.n_punti = n_punti

