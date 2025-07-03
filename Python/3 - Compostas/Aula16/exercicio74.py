from random import randint
maiorNumero = 0
menorNumero = 101
numeros = tuple(randint(1, 100) for i in range(5))

for i in range (0, len(numeros)):
    if numeros[i] > maiorNumero:
        maiorNumero = numeros[i]
    if numeros[i] < menorNumero:
        menorNumero = numeros[i]

print(numeros)
print(f'Maior número: {maiorNumero}')
print(f'Menor número: {menorNumero}')