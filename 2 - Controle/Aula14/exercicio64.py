print('Use 999 para parar')
num = int(input('Digite um número inteiro: '))
total = 0

while num != 999:
    total += num
    num = int(input('Digite um número inteiro: '))
print('O total é: ', (total))