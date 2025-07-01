numero = 0
while True:
    print('\nDigite um número negativo para parar')
    numero = float(input('Digite um número: '))
    if numero < 0:
        break
    for i in range (1, 11):
        print(f'{numero :.2f} * {i} = {numero * i :.2f}')