numero = int(input('Digite um número: '))
qtdFibonacci = int(input('Digite quantos termos da sequência de fibonacci vão ser mostrados: '))
contador = 0

a = numero
b = a

while (contador < qtdFibonacci):
    print(a)
    a, b = b, a + b
    contador += 1