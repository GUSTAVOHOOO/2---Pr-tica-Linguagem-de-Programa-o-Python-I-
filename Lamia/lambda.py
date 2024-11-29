
#lambda 

x = lambda a, b : a * b
print(x(5, 6)) #30 



# Função lambda que soma dois números
soma = lambda a, b: a + b
print(f"Soma: {soma(3, 4)}")  # Soma: 7

# Função lambda que verifica se um número é par
eh_par = lambda x: x % 2 == 0
print(f"4 é par? {eh_par(4)}")  # 4 é par? True
print(f"5 é par? {eh_par(5)}")  # 5 é par? False

# Função lambda que retorna o maior de dois números
maior = lambda a, b: a if a > b else b
print(f"Maior entre 10 e 20: {maior(10, 20)}")  # Maior entre 10 e 20: 20

# Função lambda que calcula o quadrado de um número
quadrado = lambda x: x * x
print(f"Quadrado de 5: {quadrado(5)}")  # Quadrado de 5: 25

# Usando lambda com a função map para elevar ao quadrado cada elemento de uma lista
numeros = [1, 2, 3, 4, 5]
quadrados = list(map(lambda x: x * x, numeros))
print(f"Quadrados: {quadrados}")  # Quadrados: [1, 4, 9, 16, 25]

# Usando lambda com a função filter para filtrar números pares de uma lista
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números pares: {pares}")  # Números pares: [2, 4]