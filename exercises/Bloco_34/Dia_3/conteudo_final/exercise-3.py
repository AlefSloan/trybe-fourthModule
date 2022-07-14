from abc import ABC, abstractclassmethod, abstractmethod


class Sector(ABC):
    @abstractclassmethod
    def __repr__(self):
        pass


class SupportSector(Sector):
    def __repr__(self):
        return "Setor de Suporte"


class SellerSector(Sector):
    def __repr__(self):
        return "Setor de Vendas"


class FinancialSector(Sector):
    def __repr__(self):
        return "Setor de Financeiro"


class Account(ABC):
    def __init__(self):
        self.sector = []
        self.criar_account()

    @abstractmethod
    def criar_account(self):
        pass

    def adicionar_sector(self, sector):
        self.sector.append(sector)


class SupportAccount(Account):
    def criar_account(self):
        self.adicionar_sector(SupportSector)


class SupportAndSellerAccount(Account):
    def criar_account(self):
        self.adicionar_sector(SupportSector)
        self.adicionar_sector(SellerSector)


class ManagerAccount(Account):
    def criar_account(self):
        self.adicionar_sector(SupportSector)
        self.adicionar_sector(SellerSector)
        self.adicionar_sector(FinancialSector)
