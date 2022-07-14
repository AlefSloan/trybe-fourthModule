from abc import abstractclassmethod


class Alarme:
    def __init__(self):
        self.lista_de_rotinas = []
        return 'ACORDA'

    def adicionar_rotinas(self, routine):
        self.lista_de_rotinas.append(routine)

    def despertar(self, rotinas):
        for rotina in rotinas:
            rotina.acionar()


class Routine:
    @abstractclassmethod
    def acionar(self):
        raise NotImplementedError


class LuzesRoutine(Routine):
    def __init__(self, alarme):
        self.alarme = alarme
        self.alarme.adicionar_rotinas(self)

    def acionar(self):
        print("Acendendo as Luzes")


class CafeRoutine(Routine):
    def __init__(self, alarme):
        self.alarme = alarme
        self.alarme.adicionar_rotinas(self)

    def acionar(self):
        print("Fazendo o Cafe")


class ComputadorRoutine(Routine):
    def __init__(self, alarme):
        self.alarme = alarme
        self.alarme.adicionar_rotinas(self)

    def acionar(self):
        print("Ligar o computador")
