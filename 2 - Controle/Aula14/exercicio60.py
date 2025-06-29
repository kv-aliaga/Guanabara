num = float(input('Digite um número: '))
total = 1
contador = num

while contador > 0:
    total *= contador
    contador -= 1
print(total)