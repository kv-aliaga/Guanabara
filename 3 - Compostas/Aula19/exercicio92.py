from datetime import datetime

dadosFinais = list()
dados = dict()

for i in range (0,1):
    dados ['nome'] = input('\nNome: ')
    dados['idade'] = int(input('Ano de nascimento: '))
    dados['idade'] = datetime.now().year - dados['idade']
    dados['ctps'] = int(input('Digite a CTPS: '))
    if dados['ctps'] != 0:
        dados['contratação'] = int(input('Ano de contratação: '))
        dados['salário'] = float(input('Salário: R$'))
        dados['idade da aposentadoria'] = (((dados['contratação'] - datetime.now().year) + dados['idade']) + 35)
    else:
        dados['contratação'] = 'Não possui'
        dados['salário'] = 'Não possui'
        dados['idade da aposentadoria'] = 'Não possui'
    dadosFinais.append(dados.copy())

print()

for p in dadosFinais:
    for k, v in p.items():
        print(f'O valor {k} é igual a {v}')
    print()