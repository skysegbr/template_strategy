from imposto import Imposto

class ICMS(Imposto):
    def calcula(self, orcamento):
        return orcamento.valor * 0.06
