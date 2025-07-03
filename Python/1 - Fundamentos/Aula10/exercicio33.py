num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if (num1 > num2 and num1 > num3):
    print(f'O maior número é {num1}')
    if (num2 > num3):
        print(f'O menor número é {num3}')
    else:
        print(f'O menor número é {num2}')
elif (num2 > num1 and num2 > num3):
    print(f'O maior número é {num2}')
    if (num1 > num3):
        print(f'O menor número é {num3}')
    else:
        print(f'O menor número é {num1}')
else:
    print(f'O maior número é {num3}')
    if (num2 > num1):
        print(f'O menor número é {num1}')
    else:
        print(f'O menor número é {num2}')