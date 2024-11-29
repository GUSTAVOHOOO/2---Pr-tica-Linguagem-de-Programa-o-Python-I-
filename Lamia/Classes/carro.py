# Criando classe Carro
class Carro:
    # Iniciando classe
    def __init__(self):
        self.__velocidade = 0

    # Definindo velocidade
    @property
    def velocidade(self):
        return self.__velocidade

    # Função de acelerar que incrementa velocidade
    def acelerar(self):
        self.__velocidade += 5
        return self.__velocidade

    # Função de frear que decrementa velocidade
    def frear(self):
        self.__velocidade = max(0, self.__velocidade - 5)  # Evita velocidade negativa
        return self.__velocidade

# Criando classe que herda de Carro
class Uno(Carro):
    pass

# Criando classe que herda de Carro e redefine a função acelerar
class Lancer(Carro):
    def acelerar(self):
        super().acelerar()
        return super().acelerar()

# Exemplo de uso da classe Uno
c2 = Uno()  # Atribuindo Uno ao objeto c2
print('Dirigindo Uno...')
for _ in range(4):
    print(c2.acelerar())
for _ in range(4):
    print(c2.frear())

# Exemplo de uso da classe Lancer
c1 = Lancer()  # Atribuindo Lancer ao objeto c1
print('Dirigindo Lancer...')
for _ in range(4):
    print(c1.acelerar())
for _ in range(4):
    print(c1.frear())