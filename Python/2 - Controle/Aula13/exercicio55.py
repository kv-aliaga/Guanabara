maiorPeso = 0
menorPeso = 999

for i in range (1, 6):
    peso = float(input('Digite seu peso: '))

    if (peso >= maiorPeso):
        maiorPeso = peso
    if (peso <= menorPeso):
        menorPeso = peso

print(f'Maior peso: {maiorPeso}kg')
print(f'Menor peso: {menorPeso}kg')
