
from imposto import Imposto

class ISS(Imposto):
    def calcula(self, orcamento):
        return orcamento.valor * 0.1
