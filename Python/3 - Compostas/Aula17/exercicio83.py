expressao = input('Digite uma expressão matemática: ')


qtdAbrePar = expressao.count('(')
qtdFechaPar = expressao.count(')')

if qtdAbrePar != qtdFechaPar:
    print('Errado!')
else:
    print('Certo!')

# não consegui com lista :(