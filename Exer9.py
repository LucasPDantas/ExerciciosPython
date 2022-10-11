"""
Faça um Programa que armazena em uma listaA 10 números inteiros, calcule e
mostre a soma dos quadrados dos elementos da lista.
"""
listaA = []
for numero in range(0, 10):
    listaA.append(int(input('Digite um valor inteiro: ')))

soma = 0
for valorDoQuadrado in listaA:  # FOR == PARA CADA VALOR IN == DENTRO DA LISTA
    valor = valorDoQuadrado ** 2  # CÁLCULO DE CADA VALOR DA LISTA AO QUADRADO
    soma += valor  # CALCULA A SOMA DOS VALORES AO QUADRADO
    print(f'O número {valorDoQuadrado} ao quadrado é: {valor}')
print(f'\nA soma dos valores calculados dos quadrados deu: {soma}')
