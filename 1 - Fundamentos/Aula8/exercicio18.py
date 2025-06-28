from math import sin, cos, tan, radians

angulo = float(input('Digite o valor do ângulo: '))
angulo = radians(angulo)

print(f'O seno é igual a: {sin(angulo) :.2f}º')
print(f'O cosseno é igual a: {cos(angulo) :.2f}º')
print(f'A tangente é igual a: {tan(angulo) :.2f}º')