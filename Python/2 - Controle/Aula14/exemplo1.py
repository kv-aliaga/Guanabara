# WHILE - quando não saber o limite

i = 1
while (i < 10):
    print(i)
    i += 1

# valor indeterminado, impossível de se fazer com o for
n = 1
par = 0
impar = 0

while (n != 0):
    n = int(input('Digite um número: '))
    if (n % 2 == 0):
        print('Número par')
        par += 1
    else:
        print('Número ímpar')
        impar += 1
print(f'Número par: {par}')
print(f'Número ímpar: {impar}')