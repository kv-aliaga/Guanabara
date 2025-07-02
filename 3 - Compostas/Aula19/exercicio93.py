dadosJogador = dict()
gols = 0

dadosJogador['Nome'] = input('Nome: ')
dadosJogador['Partidas Jogadas'] = int(input('Partidas Jogadas: '))
dadosJogador['Quantidade de Gols'] = 0
dadosJogador['Gols'] = []

for i in range (0, dadosJogador["Partidas Jogadas"]):
    gols = int(input(f'Quantidade de gols na partida {i + 1}: '))
    dadosJogador['Quantidade de Gols'] += gols
    dadosJogador['Gols'].append(gols)

print()
for k, v in dadosJogador.items():
    print(f'o valor {k} recebe {v}')
print()
for k, v in enumerate(dadosJogador['Gols']):
    print(f'Na partida {k + 1}, fez {v} gols')