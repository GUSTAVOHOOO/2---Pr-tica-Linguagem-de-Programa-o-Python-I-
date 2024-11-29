
# Lista de números
numeros = [1, 2, 3, 4, 5]

# Função que será aplicada a cada elemento da lista
def quadrado(x):
    return x * x

# Usando map para aplicar a função quadrado a cada elemento da lista
quadrados = list(map(quadrado, numeros))

print(f"Números: {numeros}")
print(f"Quadrados: {quadrados}")

# Usando map com uma função lambda para elevar ao cubo cada elemento da lista
cubos = list(map(lambda x: x * x * x, numeros))

print(f"Cubos: {cubos}")