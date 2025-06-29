from random import randint
numAleatorio = randint(1, 5)
escolha = int(input('Digite um número de 1 a 5: '))
print(f'Escolha do computador: {numAleatorio}', '\nEscolha certa!' if numAleatorio == escolha else '\nEscolha errada!')