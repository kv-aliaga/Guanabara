numeros = [[], []]

for i in range(1, 8):
    num = int(input(f'Digite o {i}º valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

numeros[0].sort()
numeros[1].sort()

print(f'\nNúmeros pares: {numeros[0]}')
print(f'Números ímpares: {numeros[1]}')