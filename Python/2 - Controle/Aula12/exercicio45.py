from colorama import init, Fore
from random import choice
init(autoreset=True)

print('JOKEMPÔ')

print(F"""ESCOLHA: 
{Fore.CYAN}[1]{Fore.RESET} Pedra
{Fore.CYAN}[2]{Fore.RESET} Papel
{Fore.CYAN}[3]{Fore.RESET} Tesoura""")
escolhaUsuario = int(input())

jokempoComputador = [1, 2, 3]
jokempo = ['Pedra', 'Papel', 'Tesoura']
escolhaComputador = choice(jokempo)
indice = jokempo.index(escolhaComputador)

print(f'Escolha do computador: {Fore.MAGENTA}{jokempo[indice]}')

indice += 1
if (escolhaUsuario == 1):
    if (indice == 1):
        print(f'{Fore.YELLOW}Empate')
    elif (indice == 2):
        print(f'{Fore.RED}Derrota')
    else:
        print(f'{Fore.GREEN}Vitória')
elif (escolhaUsuario == 2):
    if (indice == 2):
        print(f'{Fore.YELLOW}Empate')
    elif (indice == 3):
        print(f'{Fore.RED}Derrota')
    else:
        print(f'{Fore.GREEN}Vitória')
else:
    if (indice == 3):
        print(f'{Fore.YELLOW}Empate')
    elif (indice == 1):
        print(f'{Fore.RED}Derrota')
    else:
        print(f'{Fore.GREEN}Vitória')