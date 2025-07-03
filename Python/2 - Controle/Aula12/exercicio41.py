from colorama import init, Fore
from datetime import datetime
init(autoreset = True)

anoNascimento = int(input('Digite seu ano de nascimento: '))
idade = datetime.now().year - anoNascimento

print(f'{idade} anos')
if (idade <= 9):
    print(f'{Fore.MAGENTA}Classe Mirim')
elif (idade <= 14):
    print(f'{Fore.BLUE}Classe Infantil')
elif (idade <= 19):
    print(f'{Fore.YELLOW}Classe Junior')
elif (idade <= 20):
    print(f'{Fore.GREEN}Classe Sênior')
else:
    print(f'{Fore.WHITE}Classe Master')