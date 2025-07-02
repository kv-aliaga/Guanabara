dados = dict()
continuar = somaIdades = contador = 0
mulheres = []
idadesAcimaMedia = []
pessoas = []

while True:
    dados['nome'] = input('\nNome: ')
    dados['genero'] = input('Gênero (M/F): ').upper()
    dados['idade'] = int(input('Idade: '))
    
    somaIdades += dados['idade']
    if dados['genero'] in 'Fm':
        mulheres.append(dados['nome'])
    
    pessoas.append(dados.copy())

    continuar = input('Continuar? (S/N): ')
    if continuar in 'Nn':
        break

media = somaIdades / len(pessoas)

for pessoa in pessoas:
    if pessoa['idade'] > media:
        print()
        idadesAcimaMedia.append(pessoa['nome'])

print(f'\nPessoas cadastradas: {contador}')
print(f'Média de idade do grupo: {media} anos')
print(f'Mulheres: {mulheres}')
print(f'Pessoas com idade acima da média: {idadesAcimaMedia}')