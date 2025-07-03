from random import randint
from time import sleep

jogos = []
qtdJogos = int(input('Digite a quantidade de jogos para serem criados: '))

for i in range(qtdJogos):
    jogo = []
    while len(jogo) < 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    jogos.append(sorted(jogo))

for c, jogo in enumerate(jogos):
    sleep(1)
    print(f'Jogo {c + 1} = {jogo}')