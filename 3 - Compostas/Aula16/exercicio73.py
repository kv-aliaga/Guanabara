brasileirao = ('Flamengo', 'Cruzeiro', 'Bragantino', 'Palmeiras', 'Bahia', 'Fluminense', 'Atlético-MG', 'Botafogo', 'Mirasol', 'Corinthians', 'Grêmio', 'Ceará SC', 'Vasco da Gama', 'São Paulo', 'Santo', 'EC Vitória', 'Internacional', 'Fortaleza', 'Juventude', 'Sport Recife')

print(f'Primeiros cinco colocados: {brasileirao[:5]}')
print(f'Zona de rebaixamento: {brasileirao[-4:]}')
print(f'Três primeiros na ordem alfabética: {sorted(brasileirao[:3])}')
print(f'Posição do Corinthians: {brasileirao.index('Corinthians') + 1}º colocado')