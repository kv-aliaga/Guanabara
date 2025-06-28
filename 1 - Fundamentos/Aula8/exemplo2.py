# importando apenas umma função da biblioteca math
from math import sqrt

num1 = float(input('Digite um número: '))
raiz = sqrt(num1) # não precisa de math.sqrt

#                           arredonda para duas casas decimais
print(f'A raiz de {num1} é {raiz :.2f}')