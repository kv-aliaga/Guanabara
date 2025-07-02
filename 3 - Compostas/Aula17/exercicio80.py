numeros = []

for i in range(5):
    num = int(input(f'Digite o {i + 1}º valor: '))
    pos = 0
    
    while pos < len(numeros):
        if num < numeros[pos]:
            break
        pos += 1
    numeros.insert(pos, num)
print(numeros)