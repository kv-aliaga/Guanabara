from colorama import init, Fore, Back
init(autoreset = True)

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso / altura ** 2

print(f'IMC: {imc :.2f}')
if (imc < 18.5):
    print(f'{Fore.RED}Abaixo do peso')
elif (imc < 25):
    print(f'{Fore.GREEN}Peso ideal')
elif (imc < 30):
    print(f'{Fore.YELLOW}Sobrepeso')
elif (imc < 40):
    print(f'{Fore.RED}Obesidade')
else:
    print(f'{Fore.YELLOW} {Back.RED}Obesidade Mórbida')