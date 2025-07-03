from colorama import Fore, init
init()
from time import sleep

def lin(texto):
    tamanho = (len(texto))
    print('-='*tamanho)
    print(f'{texto :^{tamanho * 2}}')
    print('-='*tamanho)

def interactive(msg):
    return help(msg)

lin(f'{Fore.GREEN}Sistema de Ajuda PyHELP')

while True:
    resposta = input('Função ou Biblioteca > ').strip()
    
    if resposta == 'fim'.lower():
        lin(f'{Fore.RED}Até Logo!')
        break
    
    lin(f'{Fore.BLUE}Acessando o manual de comandos `{resposta}´')
    sleep(1.5)
    Fore.WHITE
    interactive(resposta)