ano = int(input('Diigite um ano: '))

if (ano % 4 == 0):
    if (ano % 100 != 0 or (ano % 100 == 0 and ano % 400 == 0)):
        print('Ano bissexto')
    else:
        print('Não é ano bissexto')
else:
    print('Não é ano bissexto')