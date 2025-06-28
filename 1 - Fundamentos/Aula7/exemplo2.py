# multiplicando strings
print('='*20) # mostra o símbolo de igual 20 vezes
print('Oi'*2) # mostra a string OiOi

# alinhamentos
#central
nome = str(input('Digite seu nome: '))
print(f'Prazer em te conhecer {nome :^20}')

# a direita
print(f'Prazer em te conhecer {nome :>20}')

# a esquerda
print(f'Prazer em te conhecer {nome :<20}')

# junta alinhamento com a multiplicação
print(f'Prazer em te conhecer {nome :=^20}')
