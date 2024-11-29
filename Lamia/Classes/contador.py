
# class Classe:
#   print("Classe criada com sucesso!") #Classe criada com sucesso! 

class Contador:
    contador = 0

    # Função para incrementar o contador
    @classmethod
    def inc(cls):
        cls.contador += 1
        return cls.contador

    # Função para decrementar o contador
    @classmethod
    def dec(cls):
        cls.contador -= 1
        return cls.contador

    # Função de incremento para n
    @staticmethod
    def mais_um(n):
        return n + 1

# Exemplo de uso da classe Contador
print(Contador.inc())  # 1
print(Contador.inc())  # 2
print(Contador.inc())  # 3
print(Contador.inc())  # 4
print(Contador.dec())  # 3
print(Contador.dec())  # 2
print(Contador.dec())  # 1
print(Contador.dec())  # 0
print(Contador.mais_um(99))  # 100