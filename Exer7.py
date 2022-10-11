"""
Faça um Programa que armazena em uma lista 5 números inteiros, mostre a soma,
a multiplicação e os números.
"""

valores = []  # VAI CRIAR UMA LISTA
for cont in range(0, 5):  # A LISTA TERÁ UM TAMANHO DE 5 ELEMENTOS
    valores.append(int(input('Digite um valor: ')))  # VAI ARMAZENAR OS ELEMENTOS DIGITADOS

for c, v in enumerate(valores):  # VAI MOSTRAR A POSIÇÃO DE CADA ELEMENTO ARMAZENADO
    print(f'Na posição {c} encontrei o valor {v}!')

soma = 0  # variável soma
multiplicar = 1  # na multiplicação não pode receber zero, se não, a resposta será zero
for numero in valores:  # for == para | in == dentro
    soma += numero
    multiplicar *= numero
print(f'\nO valor da soma é {soma}')
print(f'O valor da multiplicação é {multiplicar}')

"""
        _____OUTRA FORMA DE RESOLVER_____
def somaL(valores):
    soma = 0
    for i in valores:
        soma += i
    return soma
soma = somaL(valores)

def multiplicarL(valores):
    multiplicar = 1
    for i in valores:
        multiplicar *= i
    return multiplicar
multiplicar = multiplicarL(valores)

print(f'O valor da soma é {soma}')
print(f'O valor da multiplicação é {multiplicar}')
print('\nCheguei ao final da lista!')
"""
