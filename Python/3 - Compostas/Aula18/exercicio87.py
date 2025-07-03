matriz = [
    [], [], []
]
cont = contLinha = 0

for i in range(0, len(matriz)*3):
    num = int(input('Digite: '))
    matriz[contLinha].append(num)
    cont += 1
    if cont == 3:
        print()
        contLinha += 1
        cont = 0

cont = contLinha = totalPares = somaTerLin = maiorSegLin = 0

for i in range(0, 9):
    if matriz[contLinha][cont] % 2 == 0:
        totalPares += matriz[contLinha][cont]
    if matriz[1][cont] > maiorSegLin:
        maiorSegLin = matriz[1][cont]
    cont += 1
    if cont == 3:
        contLinha += 1
        cont = 0

for i in range(0, 3):
    somaTerLin += matriz[2][i]

for l in range(0, len(matriz)):
    print(matriz[l])

print(f'\nSOMA DOS PARES: {totalPares}')
print(f'SOMA TERCEIRA LINHA: {somaTerLin}')
print(f'MAIOR VALOR DA SEGUNDA LINHA: {maiorSegLin}')

# só deus sabe o quao difícil foi isso