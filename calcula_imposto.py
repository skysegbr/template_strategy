

class CalculadorDeImpostos:
    def realiza_calculo(self, orcamento, imposto):
        return imposto.calcula(orcamento)


if __name__ == "__main__":
    from orcamento import Orcamento
    from iss import ISS
    from icms import ICMS

    orcamento = Orcamento(500.0)

    print(CalculadorDeImpostos().realiza_calculo(orcamento, ISS()))
    print(CalculadorDeImpostos().realiza_calculo(orcamento, ICMS()))