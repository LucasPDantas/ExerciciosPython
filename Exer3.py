"""
Faça um Programa que armazena em uma lista 4 notas, mostre as notas e a média
na tela.
"""

notas = []
media = 0
qtNotas = int(input("Digite a quantidade de notas: "))
for n in range(qtNotas):
    nota = int(input("Digite uma nota: "))
    notas.append(nota)
    media += nota


print(notas)
print(media / qtNotas)
