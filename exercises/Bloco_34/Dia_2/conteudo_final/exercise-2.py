from collections.abc import Iterable, Iterator

class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        return '<%%s de %s>' % (self.valor, self.naipe)

class Baralho(Iterable):
    naipes = 'copas ouros espadas paus'.split()
    valores = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()

    def __init__(self):
        self._cartas = [
            Carta(valor, naipe)
            for naipe in self.naipes
            for valor in self.valores
        ]

    def __len__(self):
        return len(self._cartas)

    def __iter__(self):
        return BaralhoIterator(self._cartas)


class BaralhoIterator(Iterator):
    def __init__(self, cards):
        self._cards = cards
        self._count = 0

    def get_card(self, count):
        return self._cards[count]

    def __next__(self):
        card = self.get_card(self._count)

        if not card:
            raise StopIteration()
        
        self._count += 1
        return card
