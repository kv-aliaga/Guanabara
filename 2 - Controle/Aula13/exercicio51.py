primeiroTermo = float(input('Digite o primeiro  termo da progressão aritimética: '))
razão = float(input('Digite a razão: '))

total = 0
for i in range (1, 11):
    total = primeiroTermo + (i - 1) * razão
    print(f'a{i} = {primeiroTermo} + ({i} - 1) * {razão} = {total}')