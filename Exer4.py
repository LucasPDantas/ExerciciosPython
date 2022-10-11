"""
Faça um Programa que armazena em uma lista 10 caracteres, e diga quantas
consoantes foram lidas. Imprima as consoantes.
"""

contCon = []
cons = 0
print ('Informe os caracters')
for k in range(10):
 contCon.append((input('Palavra  '+ str(k+1) + ':\n')))
 char = contCon[k]
 if(char not in ('a','e','i','o','u')):
  cons += 1
print(cons)
