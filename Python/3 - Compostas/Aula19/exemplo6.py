estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = input('\nDigite a UF: ')
    estado['sigla'] = input('Digite a sigla: ')
    brasil.append(estado.copy()) # serve somente para dicionários, copia as informações sem fazer a conexão

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem {v}')
    print()