import random

resultados = dict()

for i in range(1, 5):
    nome = input(f'Digite o nome do {i}º jogador: ')
    dados = random.randint(1,6)
    resultados[nome] = dados
    
    print(f'{nome} tirou {dados}')

ranking = sorted(resultados.items(), key=lambda item: item[1], reverse=True) # peguei do oráculo rs
print('RANKING')
for i, (jogador, valor) in enumerate(ranking):
    print(f'{i + 1}º lugar: {jogador} com {valor}')