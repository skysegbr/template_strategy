#!env/bin/python

from orcamento import Orcamento
from iss import ISS
from icms import ICMS
from calcula_imposto import CalculadorDeImpostos

orcamento = Orcamento(500.0)
print(CalculadorDeImpostos().realiza_calculo(orcamento, ISS()))
print(CalculadorDeImpostos().realiza_calculo(orcamento, ICMS()))
