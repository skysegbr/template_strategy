import abc

class Imposto(abc.ABC):
    @abc.abstractmethod
    def calcula(self, orcamento):
        ...