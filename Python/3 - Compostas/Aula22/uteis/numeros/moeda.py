# EXERCICIO 109
def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')

def lin(texto):
    tamanho = len(texto)
    print('-=' * tamanho)
    print(f'{texto:^{tamanho * 2}}')
    print('-=' * tamanho)

def aumentar(num1, num2, form='S'):
    r = num1 + ((num2 / 100) * num1)
    
    if form == 'S':
        return moeda(r)
    else:
        return r

def reduzir(num1, num2, form='S'):
    r = num1 - ((num2 / 100) * num1)
    if form == 'S':
        return moeda(r)
    else:
        return r

def dobro(n, form='S'):
    r = n * 2
    if form == 'S':
        return moeda(r)
    else:
        return r

def metade(n, form='S'):
    r = n / 2
    if form == 'S':
        return moeda(r)
    else:
        return r

def resumo(preco, aumento, reducao):
    lin('RESUMO DO VALOR')
    print(f'Preço Analisado: {moeda(preco)}')
    print(f'Dobro do valor: {dobro(preco)}')
    print(f'Metade do valor: {metade(preco)}')
    print(f'{aumento}% de aumento: {aumentar(preco, aumento)}')
    print(f'{reducao}% de redução: {reduzir(preco, reducao)}')