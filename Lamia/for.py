# Exemplo de uso de for

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Loop for para iterar sobre a lista de números
for numero in numeros:
    print(f"Número: {numero}")

# Loop for para iterar sobre um range de números
for i in range(1, 6):
    print(f"Iteração {i}: {i * i}")


#  Exemplo de uso de funções
def funcao():
    print('oi') 

funcao() #oi 

def funcao(nomes):
    print('oi ' + nomes)      

funcao('Gustavo') #Gustavo oi   