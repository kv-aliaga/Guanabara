numeros = tuple(int(input(f'Digite o {i + 1}º valor da tupla: ')) for i in range(5))
qtdPares = 0

for i in range(0, len(numeros)):
    if numeros[i] % 2 == 0:
        qtdPares += 1

print(numeros)
print(f'Quantidade de vezes que o 9 apareceu: {numeros.count(9)}')
print(f'Posição do primeiro 3:', {numeros.index(3)} if 3 in numeros else 'Não apareceu')
print(f'Quantidade de números pares: {qtdPares}')