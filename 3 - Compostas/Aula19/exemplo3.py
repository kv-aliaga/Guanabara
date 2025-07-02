# exemplo de dicionários dentro de lista
netflix = [
    {
        'titulo' : 'Star Wars',
        'ano' : 1977,
        'diretor' : 'George Lucas'
    },{
        'titulo' : 'Pulp Fiction',
        'ano' : 1994,
        'diretor' : 'Quentin Tarantino'
    },{
        'titulo' : 'Black Swan',
        'ano' : 2010,
        'diretor' : 'Darren Aronofsky'
    }
]

print(netflix[0]['ano']) # pega o ano do primeiro filme, 1977
print(netflix[2]['titulo']) # pega o título do terceiro filme, Black Swan