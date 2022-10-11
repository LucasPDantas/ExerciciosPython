"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada
informação na sua respectiva lista. Imprima a idade e a altura na ordem inversa a
ordem lida.
"""
idade = []  # CRIA UMA LISTA VAZIA
for cont in range(0, 5):  # ARMAZENA 5 ELEMENTOS DENTRO DA LISTA
    idade.append(int(input('Digite a idade: ')))  # GUARDA OS ELEMENTOS DIGITADOS
idade.reverse()  # INVERTE A ORDEM QUE OS ELEMENTOS FORAM DIGITADOS
print(f'As idades digitadas foram: {idade}')

altura = []
for cont in range(0, 5):
    altura.append(float(input('Digite sua altura usando ponto (.) para separar os centimetros: ')))
altura.reverse()
print(f'As alturas digitadas foram: {altura}')
