valores = []
valores.append(6)
valores.append(7)
valores.append(8)

for i, e in enumerate(valores):
    print(f'na posicao {i} o valor {e},', end=' ') # mostra os números de valores na mesma linha enumerados

print('\n')

for cont in range(0, 5):
    valores.append(int(input('Digite o próximo valor: ')))
print(f'Novos valores: {valores}')