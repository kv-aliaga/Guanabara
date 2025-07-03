amigos = ['Jones', 'Caio', 'Otávio']

# adiciona algo na última posição
amigos.append('Pedrão')

# adiciona algo na opisção desejada
amigos.insert(2, 'Malaquias')

# deletando elementos
del amigos[0]
amigos.pop(1)
amigos.remove('Pedrão') # escrever inteiro
amigos.pop() # remove último amigo automaticamente

# deletando de forma sofisticada
if 'Otávio' in amigos:
    amigos.remove('Otávio')