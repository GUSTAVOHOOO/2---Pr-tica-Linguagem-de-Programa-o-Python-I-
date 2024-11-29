from functools import reduce

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Função que será usada pelo reduce para somar os elementos
def soma(a, b):
    return a + b

# Usando reduce para somar todos os elementos da lista
resultado_soma = reduce(soma, numeros)
print(f"Soma dos números: {resultado_soma}")

# Usando reduce com uma função lambda para multiplicar todos os elementos da lista
resultado_produto = reduce(lambda a, b: a * b, numeros)
print(f"Produto dos números: {resultado_produto}")