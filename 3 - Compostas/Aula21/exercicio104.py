def leiaInt(msg):
    while True:
        valor = input(msg)
        if valor.isnumeric():
            return int(valor)
        else:
            print('Digite um número inteiro válido')

n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')