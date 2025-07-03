filme = {
    'titulo' : 'Star Wars',
    'ano' : 1977,
    'diretor' : 'George Lucas'
}

# diferença entre chave, valores e items
print(filme.values()) # mostra todos os valores (ex.: 1977)
print(filme.keys()) # mostra todos os atributos (ex.: ano)
print(filme.items()) # mostra tudo (ex.: 'ano', 1977)

for chave, valor in filme.items():
    print(f'O {chave} é {valor}')