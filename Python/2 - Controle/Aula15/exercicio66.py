n = s = 0
cont = 1
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'A soma dos resultados é {s}')
print(f'Foram calculados {cont} números')