"""
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""
num = float(input('Informe um número:\n'))
if num < 0:
    print('O número é negativo.')
elif num == 0:
    print('Zero é um número neutro.')
else:
    print('O número é positivo')
