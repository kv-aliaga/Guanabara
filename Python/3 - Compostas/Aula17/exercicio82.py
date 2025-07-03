numeros = []
impares = []
pares = []

for i in range(1, 11):
    num = int(input(f'Digite o {i}º valor da lista: '))
    
    numeros.append(num)
    
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f'Lista completa: {numeros}')
print(f'Lista de números pares: {pares}')
print(f'Lista de números ímpares: {impares}')