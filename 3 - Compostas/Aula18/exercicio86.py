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

for l in range(0, len(matriz)):
    print(matriz[l])