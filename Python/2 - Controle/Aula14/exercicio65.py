num = int(input('Digite um número: '))
continuar = input('Quer continuar? (S/N) ').lower()
total = 0
maior = 0
qtdNumeros = 0
menor = 999 * pow(10, 99)

while continuar != 'n':
    total += num
    qtdNumeros += 1
    if (num < menor):
        menor = num
    if (num > maior):
        maior = num
    num = int(input('\nDigite um número: '))
    continuar = input('Quer continuar? (S/N) ').lower()

print(f'Maior número: {maior}')
print(f'Menor número: {menor}')
print(f'Média: {total/qtdNumeros}')