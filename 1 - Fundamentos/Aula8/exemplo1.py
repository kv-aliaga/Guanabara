# importando toda a biblioteca math
import math

num1 = int(input('Digite um número: '))
raiz = math.sqrt(num1)

#                                     mostra o arredondamento da raíz quadrada de num1
print(f'A raíz quadrada de {num1} é {math.ceil(raiz)}')