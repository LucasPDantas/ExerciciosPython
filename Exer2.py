"""
Faça um Programa que armazena em uma lista 10 números reais e mostre-os na
ordem inversa.
"""

numRea = []

for b in range(5):
    numero = int(input("Digite um numero: "))
    numRea.append(numero)


numRea.reverse()
print(numRea)
