from random import randint
from colorama import init, Fore
init(autoreset = True)

numeroAleatorio = randint(1,50)
numero = int(input('Digite um número de 1 a 50: '))

print(Fore.MAGENTA + f'O número escolhido pelo compuador foi: {numeroAleatorio}')
if (numero > numeroAleatorio):
    print(f'{Fore.RED}O número digitado é maior que o número escolhido')
elif (numero < numeroAleatorio):
    print(f'{Fore.BLUE}O número digitado é menor que o número escolhido')
else:
    print(f'{Fore.GREEN}Os números são iguais!')