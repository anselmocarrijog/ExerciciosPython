"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
Faça um Programa que leia três números e mostre o maior deles.
"""
num = float(input('Informe a primeira nota:\n'))
num1 = float(input('Informe a segunda nota:\n'))
media = (num + num1)/2
if 7 <= media <= 9:
    print('Aprovado...')
elif media < 7:
    print('Reprovado...')
else:
    print('Aprovado com Distinção...')
