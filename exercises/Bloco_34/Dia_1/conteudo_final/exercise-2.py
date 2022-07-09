import math
from collections import Counter


class Estatistica:
    def init(self):
        self.__media = None
        self.__mediana = None
        self.__moda = None

    @classmethod
    def media(cls, array_of_numbers):
        media = 0
        for x in array_of_numbers:
            media += x
        cls.__media = media / len(array_of_numbers)
        return cls.__media

    @classmethod
    def mediana(cls, array_of_numbers):
        sorted_list = sorted(array_of_numbers)
        media = math.floor(len(sorted_list) / 2)
        if len(sorted_list) % 2 == 0:
            cls.__mediana = (sorted_list[media] + sorted_list[media - 1]) / 2
            return (sorted_list[media] + sorted_list[media - 1]) / 2
        else:
            cls.__mediana = sorted_list[media]
            return sorted_list[media]

    @classmethod
    def moda(cls, array_of_numbers):
        counter = Counter(array_of_numbers)
        return counter.most_common()[0][0]
