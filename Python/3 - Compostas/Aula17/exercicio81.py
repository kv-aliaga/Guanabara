numeros = []

qtdNumeros = cont = 0

while True:
    cont += 1
    num =  int(input(f'Digite o {cont}º número: '))
    
    numeros.append(num)
    qtdNumeros += 1
    
    continuar = input('Deseja continuar? ').upper()
    if continuar[0] == 'N':
        break

numeros.sort(reverse=True)

print(f'Quantidade de números digitados: {qtdNumeros}')
print(f'Lista Decrescente: {numeros}')
print(f'Quantidade de 5 na lista: ', f'{numeros.count(5)}' if 5 in numeros else 'Não aparece')
