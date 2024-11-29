# Exemplo de uso de while
import random

# Inicializando variáveis
tentativas = 0
numero_secreto = random.randint(1, 10)
adivinhou = False

print("Tente adivinhar o número secreto entre 1 e 10!")

# Loop while
while not adivinhou:
    tentativas += 1
    palpite = int(input("Digite seu palpite: "))

    if palpite == numero_secreto:
        adivinhou = True
        print(f"Parabéns! Você adivinhou o número secreto {numero_secreto} em {tentativas} tentativas.")
    elif palpite < numero_secreto:
        print("O número secreto é maior. Tente novamente.")
    else:
        print("O número secreto é menor. Tente novamente.")