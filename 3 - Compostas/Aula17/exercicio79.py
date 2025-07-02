numeros = []
i = 1

while i <= 5:
    num = int(input(f'Adicione o {i}º número na lista: '))
    
    if num not in numeros:
        numeros.append(num)
        i += 1
    else:
        print('Digite apenas números diferentes uns dos otros')

numeros.sort()
print(numeros)