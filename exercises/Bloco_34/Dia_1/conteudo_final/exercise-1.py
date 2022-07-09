class TV:
    def __init__(self, tamanho):
        self.__volume = 50
        self.__canal = 1
        self.__tamanho = tamanho
        self.__ligada = False

    def aumentar_volume(self):
        if self.__volume > 99:
            self.__volume = 99
        else:
            self.__volume += 1

    def diminuir_volume(self):
        if self.__volume < 0:
            self.__volume = 0
        else:
            self.__volume -= 1

    def modificar_canal(self, canal):
        if 0 > canal > 99:
            raise ValueError('Esse canal não existe!')
        else:
            self.__canal = canal

    def ligar_desligar(self):
        self.__ligada = not self.__ligada
