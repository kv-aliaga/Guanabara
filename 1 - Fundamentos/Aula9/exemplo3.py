frase = '   Rei Kavhsao Jones III   '

print(frase.strip()) # remove espaços 'inúteis' no início e fim
print(frase.rstrip()) # remove apenas na direita
print(frase.lstrip()) # remove apenas na esquerda

print(frase.split()) # cria uma lista com todas as palavras de uma lista de caracteres
print('...'.join(frase)) # para cada caractere adiciona ...

frase = frase.split()
print(frase[0])