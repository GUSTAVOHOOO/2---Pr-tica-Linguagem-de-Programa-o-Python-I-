class Produto:
    # Função para inicializar a classe
    def __init__(self, nome, preco=1.99, desc=0):
        self.nome = nome
        self.__preco = preco
        self.desc = desc

    # Função para definir o desconto
    @property
    def preco_final(self):
        return (1 - self.desc) * self.__preco

    # Função para obter o preço
    @property
    def preco(self):
        return self.__preco

    # Função para aceitar modificações se o novo preço for maior que zero
    @preco.setter
    def preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco
        else:
            raise ValueError("O preço deve ser maior que zero")

# Exemplo de uso da classe Produto
p1 = Produto('Caneta', 10.00, 0.1)
p2 = Produto('Caderno', 17.00, 0.5)

# Tentativa de definir um preço inválido
try:
    p1.preco = 0  # Esta atribuição será desconsiderada pelo programa
except ValueError as e:
    print(e)

# Atribuindo novo preço ao caderno
p2.preco = 18.00

print(f'Produto: {p1.nome}, Preço: {p1.preco}, Desconto: {p1.desc}, Preço final: {p1.preco_final}')
print(f'Produto: {p2.nome}, Preço: {p2.preco}, Desconto: {p2.desc}, Preço final: {p2.preco_final}')