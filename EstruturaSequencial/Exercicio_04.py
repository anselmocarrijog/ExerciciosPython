"""Faça um Programa que peça as 4 notas bimestrais e mostre a média."""
cont = 0
soma = []
while cont < 4:
    print('Digite um número:')
    num = int(input())
    soma.append(num)
    cont = cont + 1

valor = sum(soma)
print(valor)
