from random import randint
from colorama import init, Fore
from time import sleep
init()

print('Par ou Ímpar')

n = vitorias = nComp = escolha = 0
while True:
    escolha = input('Escolha par ou ímpar (P/I): ').upper()
    n = int(input('Digite um número de 0 a 10: '))
    nComp = randint(0, 10)
    print(f'A escolha do computador foi... ', end='')
    sleep(1)
    print(nComp)
    if escolha[0] == 'P':
        if (n + nComp) % 2 == 0:
            print(Fore.GREEN, 'Vitória!')
            vitorias += 1
        else:
            print(Fore.RED, 'Derrota...')
            break
    elif escolha[0] in ['I', 'Í']:
        if (n + nComp) % 2 != 0:
            print(Fore.GREEN, 'Vitória!')
            vitorias += 1
        else:
            print(Fore.RED, 'Derrota...')
            break
    else:
        print(Fore.YELLOW, 'Seleção errada... Tente novamente')
    Fore.RESET
print(f'Antes de perder você venceu{Fore.GREEN}  {vitorias} vitórias {Fore.RESET} consecutiivas!')