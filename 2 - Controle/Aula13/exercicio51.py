primeiroTermo = float(input('Digite o primeiro  termo da progressão aritimética: '))
razao = float(input('Digite a razão: '))

total = 0
for i in range (1, 11):
    total = primeiroTermo + (i - 1) * razao
    print(f'a{i} = {primeiroTermo} + ({i} - 1) * {razao} = {total}')