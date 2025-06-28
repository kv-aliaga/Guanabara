from colorama import init, Fore
from datetime import datetime
init(autoreset = True)

anoNascimento = int(input('Digite o ano do seu nascimento: '))
idade = datetime.now().year - anoNascimento

if (idade < 18):
    print(f'{Fore.BLUE}Você ainda não precisa se alistar. Faltam {18 - idade} anos para sua época de alistamento')
elif (idade == 18):
    print(f'{Fore.RED}Está na hora de se alistar')
else:
    print(f'{Fore.GREEN}Você não precisa mais se alistar. Se passaram {idade - 18} anos desde a sua época de alistamento')