import math

num1 = float(input('Digite um número real: '))

print(f'O número {num1} tem a parte inteira {int(num1//1)}')
print(f'O número {num1} tem a parte inteira {math.trunc(num1)}')