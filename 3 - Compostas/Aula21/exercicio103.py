def ficha(nome = '', gols = ''):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    return f'O jogador {nome} fez {gols} gols no campeonato.'

nome = input('Nome: ')
gols = (input('Gols: '))
print(ficha(nome, gols))