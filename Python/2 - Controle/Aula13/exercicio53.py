frase = input('Digite uma frase: ')
invertida = frase[::-1].split()

fraseFinal = ''
for i in range(0, len(invertida)):
    fraseFinal += invertida[i]

if (fraseFinal == fraseFinal[::-1]):
    print('É um palíndromo!')
    print(fraseFinal)
else:
    print('Não é um palíndromo')
    print(f'Frase normal: {fraseFinal[::-1]}')
    print(f'Frase invertida: {fraseFinal}')