from time import sleep

def contador(inicio, fim, passo):
    # conta de 1 a 10 pulando de 1 a 1
    for i in range(1, 10):
        print(i, end=' ')
    print('FIM!\n')

    # conta de 10 a 1 pulando de 2 em 2
    for i in range(10, 0, -2):
        print(i, end=' ')
    print('FIM!\n')

    # personalizado
    for i in range(inicio, fim, passo):
        print(i, end=' ')
    print('FIM!\n')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
if p == 0:
    p = -1
else:
    p = abs(p)
f += 1

contador(i, f, p)