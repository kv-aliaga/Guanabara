from random import randint

numAleatorio = randint(1, 10)
escolha = int(input('Digite um número de 1 a 10: '))
tentativas = 1

while (numAleatorio != escolha):
    print('Escolha errada!', 'Tente um número menor' if numAleatorio < escolha else 'Tente um número maior')
    tentativas += 1
    escolha = int(input('\nDigite um número de 1 a 10: '))

print(f'Você acertou em {tentativas} tentativas!')