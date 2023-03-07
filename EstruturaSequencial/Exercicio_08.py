"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
A: o produto do dobro do primeiro com metade do segundo .
B: a soma do triplo do primeiro com o terceiro.
C: o terceiro elevado ao cubo.
"""
num1 = int(input('Digite um numero inteiro:\n'))
num2 = int(input('Digite um numero inteiro:\n'))
num3 = float(input('Digite um numero Real:\n'))

print('O produto é', (2 * num1) * (num2 / 2))
print('A soma é:', (3 * num1) * num3)
print('Elevado ao cubo é:', num3**3)
