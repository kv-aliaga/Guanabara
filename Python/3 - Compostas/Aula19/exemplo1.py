dados =  dict()
dados = {
    'nome':'Jones',
    'idade': 69
}

# em dicionários, append não funciona para adicionar, ao invés disso, usar:
dados['genero'] = 'M' # cria automaticamente

# e para deletar...
del dados['genero']

print(dados['nome'])
print(dados['idade'])