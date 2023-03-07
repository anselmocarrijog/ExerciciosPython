"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

"""
letra = str(input('Digite uma letra:\n'))
if letra.isalpha():
    if letra == 'a':
        print('Você digitou uma Vogal...')
    elif letra == 'e':
        print('Você digitou uma Vogal...')
    elif letra == 'i':
        print('Você digitou uma Vogal...')
    elif letra == 'o':
        print('Você digitou uma Vogal...')
    elif letra == 'u':
        print('Você digitou uma Vogal...')
    else:
        print('Você digitou uma Consoante...')
else:
    print('Não é aceito Números...')