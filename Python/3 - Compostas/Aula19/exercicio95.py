jogadores = []  # Lista de jogadores

while True:
    dadosJogador = dict()
    dadosJogador['Nome'] = input('Nome: ')
    total_partidas = int(input('Partidas Jogadas: '))
    dadosJogador['Gols'] = []
    dadosJogador['Quantidade de Gols'] = 0

    for i in range(total_partidas):
        gols = int(input(f'Quantidade de gols na partida {i + 1}: '))
        dadosJogador['Gols'].append(gols)
        dadosJogador['Quantidade de Gols'] += gols

    jogadores.append(dadosJogador.copy())

    continuar = input('Deseja adicionar outro jogador? (S/N): ').strip().upper()
    if continuar == 'N':
        break

print('-=' * 30)
print(f'{"Cod.":<6}{"NOME":<10}{"GOLS":<10}{"TOTAL":>2}')
print('-' * 60)
for i, jogador in enumerate(jogadores):
    print(f'{i:<6}{jogador["Nome"]:<10}{str(jogador["Gols"]):<10}{jogador["Quantidade de Gols"]:>2}')

while True:
    outro = int(input('Mostrar levantamento de outro jogador? (Digite seu código): '))
    if outro == 999:
        break
    else:
        for k, v in enumerate(jogadores[outro]['Gols']):
            print(f'Na partida {k + 1}, fez {v} gols')
