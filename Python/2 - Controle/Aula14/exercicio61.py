primeiroTermo = float(input('Digite o primeiro termo da progressão aritimética: '))
razao = float(input('Digite a razão: '))
contador = 1
total = 0

while contador <= 10:
    total = primeiroTermo + (contador - 1) * razao
    print(f'a{contador} = {primeiroTermo} + ({contador} - 1) * {razao} = {total}')
    contador += 1