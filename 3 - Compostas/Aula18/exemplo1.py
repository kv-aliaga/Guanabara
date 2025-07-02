# exemplo de lista dentro de lista
dados = list()
pessoas = list()

dados.append('Maria')
dados.append(32)

dados.append('Pedro')
dados.append(15)

dados.append('João')
dados.append(23)


# adiciona as infromações de dados dentro de pessoa
pessoas.append(dados[0:2]) # copia os dados e adiciona em pessoa

print(dados[:])
print(pessoas[:]) # comportamento de conjuntos
print(pessoas[0]) # Maria, 32