nome = preco = nomeMenor = qtdMaior1000 = continuar = total = 0
precoMenor  = 9999999999 * pow(999, 9)

while True:
    nome = input('\nDigite o nome do produto: ')
    preco = float(input(f'Digite o preço de {nome}: R$'))
    continuar = input('Continuar? (S/N) ').upper()
    
    if preco > 1000:
        qtdMaior1000 += 1
    if preco < precoMenor:
        precoMenor = preco
        nomeMenor = nome
    total += preco
    if continuar[0] == 'N':
        break

print('RESULTADOS FINAIS')
print(f'Total gasto: R${total}')
print(f'Produtos mais caros que R$1000: {qtdMaior1000}')
print(f'Produto mais barato: {nomeMenor}')