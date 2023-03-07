"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

sexo = input(('Informe f para feminino e m para masculino:'))
if sexo == 'f':
    print('Sexo Feminino...')
elif sexo == 'm':
    print('Sexo Masculino...')
else:
    print('Sexo Inválido...')
    print('Digite somente F para feminino ou M para masculino...')
print('Fim programa.')
