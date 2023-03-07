"""
Faça um Programa que peça dois números e imprima o maior deles.
"""
num = float(input('Informe o primeiro número:\n'))
num1 = float(input('Informe o segundo número:\n'))

if num > num1:
    print('O maior número é {:.1f}'.format(num),', o primeiro digitado.')
else:
    print('O maior número digitado foi {:.1f}'.format(num1),', o segundo digitado.')