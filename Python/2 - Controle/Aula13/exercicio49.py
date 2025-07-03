numero = int(input('Digite um número: '))
multiplo = int(input(f'Digite até qual número {numero} vai ser multiplicado: '))

for i in range (1, multiplo + 1):
    print(f'{numero} * {i} = {numero * i}')