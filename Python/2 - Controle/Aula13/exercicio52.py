numero = int(input('Digite um número: '))

if (numero < 2):
    print('Não é primo.')
else:
    for i in range(2, int(numero ** (1/2) + 1)):
        if (numero % i == 0):
            print('Não é primo.')
            break
        else:
            print('É primo.')
            break