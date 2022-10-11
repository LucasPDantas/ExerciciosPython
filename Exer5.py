"""
Faça um Programa que leia 20 números inteiros e armazene-os numa lista.
Armazene os números pares na lista PAR e os números IMPARES na lista impar.
Imprima os três vetores.
"""

par = []
impar = []
numerosDigitados = []
numero = 0
for h in range(20):
  numerosDigitados.append((int(input('Numero: ' + str(h+1) + ':\n'))))
  numero = numerosDigitados[h]

  if(numero%2 == 0):
   par.append(numero)
  else:
   impar.append(numero)

print(f"Numero Digitados \n{numerosDigitados}")
print(f"Numeros pares \n{par}")
print(f"Numeros impar \n{impar}")
