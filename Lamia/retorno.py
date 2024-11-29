#exemplo de funcao com retorno
# Definindo uma função que soma dois números
def soma(a, b):
    return a + b

# Definindo uma função que imprime uma saudação
def saudacao(nome):
    print(f"Olá, {nome}!")

# Definindo uma função que verifica se um número é par ou ímpar
def par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

# Chamando as funções
resultado_soma = soma(3, 5)
print(f"Soma: {resultado_soma}")

saudacao("Gustavo")

resultado_par_ou_impar = par_ou_impar(7)
print(f"O número 7 é {resultado_par_ou_impar}")