numeros = list(range(5, 11)) # cria lista de 5 até 10
numeros.sort() # ordena valores de forma crescente, mudando seus índices, algo impossível com tuplas
numeros.sort(reverse=True) # faz o mesmo com a ordem decrescente

print(numeros)