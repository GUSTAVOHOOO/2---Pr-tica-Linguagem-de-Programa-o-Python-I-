
# Exemplo de uso de if, elif e else
import random

# Gerar dados aleatórios
idade = random.randint(1, 100)
saldo_bancario = random.uniform(0, 5000)
tem_carteira_de_motorista = random.choice([True, False])

print(f"Idade: {idade}")
print(f"Saldo Bancário: {saldo_bancario:.2f}")
print(f"Tem Carteira de Motorista: {tem_carteira_de_motorista}")

# Exemplificação com if, elif e else
if idade < 18:
    status_idade = "Menor de idade"
elif 18 <= idade < 65:
    status_idade = "Adulto"
else:
    status_idade = "Idoso"

if saldo_bancario < 1000:
    status_financeiro = "Saldo baixo"
elif 1000 <= saldo_bancario < 3000:
    status_financeiro = "Saldo médio"
else:
    status_financeiro = "Saldo alto"

if tem_carteira_de_motorista:
    status_carteira = "Pode dirigir"
else:
    status_carteira = "Não pode dirigir"

print(f"Status de Idade: {status_idade}")
print(f"Status Financeiro: {status_financeiro}")
print(f"Status de Carteira de Motorista: {status_carteira}")
