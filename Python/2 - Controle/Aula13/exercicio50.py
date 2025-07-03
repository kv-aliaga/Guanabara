total = 0
for i in range(1, 7):
    numero = int(input('Digite um número: '))
    if (numero % 2 == 0):
        total += numero
print(f'A soma dos números pares digitados é igual a: {total}')