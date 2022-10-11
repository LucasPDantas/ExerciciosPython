"""
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene
numa lista a média de cada aluno, imprima o número de alunos com média maior
ou igual a 7.0.
"""

def calcMedia(aluno):
    print(f'Notas do aluno {aluno}')
    total = 0
    for a in range(2):
        total += float(input(f'Digite a {a + 1}ª nota: '))
    return total / 2  # Retorna o valor para a variavel que a chamou.


def mostraMedia(lst):
    aprovado = 0
    for x in lst:
        if x >= 7:
            aprovado += 1
    print(f'Lista com o resultado das medias: {lst}')
    print(f'Há {aprovado} aluno(s) com media superior a 7,0')


medias = list()
for a in range(5):
    medias.append(calcMedia(a + 1))
    print()

mostraMedia(medias)
