# Solução do Desafio
def calcularSaldo(numA, numB):
    return numA - numB

numA = int(input("Digite o seu número de vitórias: "))
numB = int(input("Digite o seu número de derrotas: "))

saldoVitorias = calcularSaldo(numA, numB)

if saldoVitorias <= 10:
    nivel = 'Ferro'
elif saldoVitorias < 21:
    nivel = 'Bronze'
elif saldoVitorias < 51:
    nivel = 'Prata'
elif saldoVitorias < 81:
    nivel = 'Ouro'
elif saldoVitorias < 91:
    nivel = 'Diamante'
elif saldoVitorias < 101:
    nivel = 'Lendário'
else:
    nivel = 'imortal'


print(f"O Herói tem de saldo de {saldoVitorias} está no nível de {nivel}.")