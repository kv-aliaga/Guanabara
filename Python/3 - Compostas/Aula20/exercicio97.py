def escreva(texto):
    tamanho = (len(texto))
    print('-='*tamanho)
    print(f'{texto :^{tamanho * 2}}')
    print('-='*tamanho)

escreva('Jones morreu aqui!')