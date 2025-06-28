from random import randint

numAleatorio = randint(1, 5)
escolha = int(input('Digite um número de 1 a 5: '))

if (numAleatorio == escolha):
    print('Escolha certa!')
else:
    print('Escolha errada!')