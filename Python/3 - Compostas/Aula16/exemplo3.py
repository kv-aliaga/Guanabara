lanche = ('Hamburguer', 'Pizza', 'Lasanha')

# forma 1 de for com tupla
for l in lanche:
    print(f'Eu comi {l}') # mostra cada elemento de lanche
print('Eu comi pra caramba!')

print()

# forma 2 de for com tupla
for cont in range(0, len(lanche)):
    print(f'No meu {cont + 1}º prato eu comi {lanche[cont]}')
print('Eu comi pra caramba!')

# forma 3 de for com tupla
for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posicao}')