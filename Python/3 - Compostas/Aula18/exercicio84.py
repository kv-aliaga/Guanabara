pessoas = [[], []]
maiorPeso = [0.00001]
qtdPessoas = continuar = 0

while True:
    nome = input('\nNome: ')
    peso = float(input('Peso: '))
    
    pessoas[0].append(nome)
    pessoas[1].append(peso)
    qtdPessoas += 1
    continuar = input('Continuar? (S/N): ').upper().strip()
    if continuar == 'N':
        break

pessoas[1].sort
for i in range(0, qtdPessoas):
    if pessoas[1][i] > maiorPeso[0]:
        maiorPeso.append(pessoas[0][i])

print(f'\nQuantidade de pessoas: {qtdPessoas}')
print(f'Pessoas mais pesadas: {maiorPeso}')
print(pessoas[1])