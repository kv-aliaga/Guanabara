# criando defs com parâmetros epacotados
from time import sleep
def contador(* numero): # sinal que os parâmetros são indeterminados
    for n in numero:
        print(n)
        sleep(1)

contador(1, 2, 3, 5, 5, 5)

# defs podem ser usados com outras funções
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

valores = [1, 3, 4, 5, 6, 7]
dobra(valores)
print(valores)