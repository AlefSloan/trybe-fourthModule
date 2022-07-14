from abc import ABC, abstractclassmethod


class ImpostoInterface(ABC):
    @classmethod
    @abstractclassmethod
    def calcular(cls, valor):
        raise NotImplementedError


class ImpostoISS(ImpostoInterface):
    @classmethod
    def calcular(cls, valor):
        return valor * 0.1


class ImpostoICMS(ImpostoInterface):
    @classmethod
    def calcular(cls, valor):
        return valor * 0.06


class ImpostoPIS(ImpostoInterface):
    @classmethod
    def calcular(cls, valor):
        return valor * 0.0065


class ImpostoCOFINS(ImpostoInterface):
    @classmethod
    def calcular(cls, valor):
        return valor * 0.03


class Orcamento:
    def __init__(self, valor):
        self.valor = valor

    def calcular_imposto(self, imposto):
        return imposto.calcular(self.valor)


orcamento = Orcamento(1000)
print(f"ISS: {orcamento.calcular_imposto(ImpostoISS)}")
print(f"ICMS: {orcamento.calcular_imposto(ImpostoICMS)}")
print(f"PIS: {orcamento.calcular_imposto(ImpostoPIS)}")
print(f"COFINS: {orcamento.calcular_imposto(ImpostoCOFINS)}")
