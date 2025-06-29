primeiroTermo = float(input('Digite o primeiro termo da progressão aritimética: '))
razao = float(input('Digite a razão: '))
contador = 1
total = 0
termos = 11

while contador != termos:
    total = primeiroTermo + (contador - 1) * razao
    print(f'a{contador} = {primeiroTermo} + ({contador} - 1) * {razao} = {total}')
    contador += 1
    if contador == termos:
        maisTermos = int(input('Deseja mostrar mais quantos termos? '))
        termos += maisTermos    