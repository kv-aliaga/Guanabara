def fatorial(num1 = 1):
    f = 1
    for i in range(num1, 0, -1):
        f *= i
    return f

n = int(input('Número: '))
print(f'O fatorial de {n} é {fatorial(n)}')

def parOuImpar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

n = int(input('\nNúmero: '))
print(f'O número {n} é:', 'Par' if parOuImpar(n) == True else 'Ímpar')