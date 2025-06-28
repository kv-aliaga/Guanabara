from colorama import init, Fore
init(autoreset = True)

lado1 = float(input('Digite o primeiro lado: '))
lado2 = float(input('Digite o segundo lado: '))
lado3 = float(input('Digite o terceiro lado: '))

if (lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1):
    if (lado1 == lado2 == lado3):
        print(f'{Fore.RED}Triângulo Equilátero')
    elif (lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
        print(f'{Fore.GREEN}Triângulo Isóceles')
    else:
        print(f'{Fore.BLUE}Triângulo Escaleno')
else:
    print('Não pode formar um triângulo')