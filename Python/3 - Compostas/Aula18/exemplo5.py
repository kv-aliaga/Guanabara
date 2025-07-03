ozmano = list()
dados = list()
totalMenor = totalMaior = 0

for c in range(1, 4):
    dados.append(input(f'\nNome da {c}ª pessoa: '))
    dados.append(int(input(f'Idade da {c}ª pessoa: ')))
    
    ozmano.append(dados[:])
    dados.clear() # limpa as informações de dados

print()

for mano in ozmano:
    if mano[1] >= 18:
        print(f'{mano[0]} é maior de idade')
        totalMaior += 1
    else:
        print(f'{mano[0]} é menor de idade')
        totalMenor += 1

print(f'\nTemos {totalMaior} maiores de idade e {totalMenor} menores de idade nozmano')