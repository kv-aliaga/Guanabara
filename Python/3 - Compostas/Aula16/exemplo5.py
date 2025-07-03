a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b

print(c) # mostra c inalterado
print(sorted(c)) # mostra como em conjuntos
print(c.count(5)) # conta quantas vezes o 5 aparece
print(c.index(2)) # mostra a posição da primeira ocorrência de 2
print(c.index(2, 1)) # mostra a posição da próxima ocorrência de 2 depois de 0
del(c) # única forma de alterar tupla, apagando-a