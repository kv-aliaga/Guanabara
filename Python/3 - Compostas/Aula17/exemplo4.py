# exemplo de conexão de listas
a = [2, 4, 3, 7]
b = a
b[2] = 8 # muda o terceiro valor para 8
print(a) # o terceiro valor aqui também é 8, as listas estão conectadas

# exemplo de cópia de listas
b = a[:] # copia os valores sem fazer conexão
b[2] = 6
print(a) # continua sendo [2, 4, 8, 7]