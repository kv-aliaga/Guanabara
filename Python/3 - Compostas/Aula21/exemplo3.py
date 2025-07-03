# PARÂMETROS OPCIONAIS
def somar (a, b, c = 0): # no caso de c não ter sido declarado, o código não apresenta problemas já que ele é opcional
    s = a + b + c
    print(f'A soma é {s}')

somar(3, 5) # coloca apenas a, b

# RETORNO

def subtrair (a=0, b=0, c=0):
    s = a - b - c
    return s # guarda na memória s

r1 = subtrair(1, 7, 5)
r2 = subtrair(2, 5)
r3 = subtrair(100, 50)
print(f'Os resultados são: {r1}, {r2}, {r3}') # servem para melhor personalização dos resultados