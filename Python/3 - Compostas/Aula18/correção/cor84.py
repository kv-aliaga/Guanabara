temporario = []
principal  = []
maior = menor = 0

while True:
    temporario.append(input('\nNome: '))
    temporario.append(float(input('Peso: ')))
    
    if len(principal) == 0:
        maior = menor = temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor:
            menor = temporario[1]
    
    principal.append(temporario[:])
    temporario.clear()
    
    continuar = input('Continuar? (S/N): ')
    if continuar in 'Nn':
        break

print('\n', '-='*30)
print(f'Você cadastrou: {len(principal)} pessoas')
print(f'O maior peso é: {maior}kg, com as pessoas:', end='')
for p in principal:
    if p[1] == maior:
        print(f' [{p[0]}]', end='')
print()
print(f'O menor peso é: {menor}kg, com as pessoas:', end='')
for p in principal:
    if p[1] == menor:
        print(f' [{p[0]}]', end='')