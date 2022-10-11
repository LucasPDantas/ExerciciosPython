"""
Faça um Programa que armazena em duas listas 10 elementos cada. Gere uma
terceira lista 20 elementos, cujos valores deverão ser compostos pelos elementos
intercalados dos dois outros vetores.
"""
listaA = []
for a in range(0, 5):
    listaA.append(str(input('Lista 1: ')))
print(f'\nlista A {listaA}')
listaB = []
for b in range(0, 5):
    listaB.append(str(input('Lista 2: ')))
print(f'\nlista B {listaB}')
#print(f'\nlista C: {listaA + listaB}')
