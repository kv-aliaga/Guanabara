calculoMedia = dict()
resultado = list()

calculoMedia['nome'] = input('Nome: ')
calculoMedia['media'] = float(input(f'Média de {calculoMedia["nome"]}: '))

if calculoMedia['media'] > 7 :
    calculoMedia['situacao'] = 'Aprovado'
elif calculoMedia['media'] > 5 :
    calculoMedia['situacao'] = 'Recuperação'
else:
    calculoMedia['situacao'] = 'Reprovado'

resultado.append(calculoMedia.copy())

for a in resultado:
    for k, v in a.items():
        print(f'{k} é igual a {v}')
    print()