total = 0
for i in range (1, 501):
    if (i % 2 != 0 and i % 3 == 0):
        total += i
print(f'A soma dos números ímpares múltiplos de 3 de 1 a 500 é: {total}')