class Eletrodomestico:
    def __init__(self, cor, potencia, voltagem, preco):
        self.preco = preco
        self.__cor = cor
        self.__potencia = potencia
        self.__voltagem = voltagem
        self.__ligado = False
        self.__amperagem_atual_no_motor = 0
        self.__velocidade_maxima = 3

    def ligar(self, velocidade):
        self.__velocidade = velocidade
        self.__amperagem_atual_no_motor = (
            (self.__potencia / self.__voltagem) / self.__velocidade_maxima
        ) * velocidade
        self.__ligado = True

    def desligar(self):
        self.__ligado = False
        self.__velocidade = 0

    def esta_ligado(self):
        return self.__ligado


class Liquidificador(Eletrodomestico):  # Exemplo de Herança
    def __init__(self, cor, potencia, voltagem, preco):
        # chamando o método da classe mãe
        super().__init__(cor, potencia, voltagem, preco)


class Geladeira(Eletrodomestico):
    def __init__(self, cor, potencia, voltagem, preco, quantidade_de_portas=1):
        super().__init__(cor, potencia, voltagem, preco)
        # sobrescrita do método da classe mãe
        self.quantidade_de_portas = quantidade_de_portas


class Microondas(Eletrodomestico):
    def __init__(self, cor, potencia, voltagem, preco, quantidade_de_portas=1):
        super().__init__(cor, potencia, voltagem, preco)
        self.quantidade_de_portas = quantidade_de_portas


microondas = Microondas('Branco', 220, 50, 1000)
print(microondas.esta_ligado())
microondas.ligar(1)
print(microondas.esta_ligado())


class Batedeira(Eletrodomestico):
    def __init__(self, cor, potencia, voltagem, preco):
        super().__init__(cor, potencia, voltagem, preco)


batedeira = Microondas('Azul', 220, 50, 500)
print(batedeira.esta_ligado())
batedeira.ligar(1)
print(batedeira.esta_ligado())


class Fogão(Eletrodomestico):
    def __init__(self, cor, potencia, voltagem, preco):
        super().__init__(cor, potencia, voltagem, preco)


fogão = Microondas('Verde', 220, 50, 200)
print(fogão.esta_ligado())
fogão.ligar(1)
print(fogão.esta_ligado())
