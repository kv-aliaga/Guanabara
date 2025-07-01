produtos = ('Sabão', 9.1, 'Borracha', 10.9, 'Barbatuque', 85.69)
i = p = 0

print(f'LISTAGEM DE PREÇOS')
for i in range(0, len(produtos), 2):
    nome = produtos[i]
    preco = produtos[i + 1]
    print(f'{nome:.<20}R${preco}')