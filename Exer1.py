"""
Faça um Programa que armazena em uma lista 5 números inteiros e mostre-os.
"""

cont = 0
numInt = []
for a in range(5):
    numero = int(input("Digite um numero: "))
    numInt.append(numero)
    cont += 1

print(numInt)
