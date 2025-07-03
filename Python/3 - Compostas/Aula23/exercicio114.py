import requests
from colorama import Fore, init
init()

def esta_online(url):
    try:
        resposta = requests.get(url, timeout=5)
        if resposta.status_code == 200:
            print(f'{Fore.GREEN}O SITE TA NO AR!')
        else:
            print(f'{Fore.YELLOW}O site respondeu com {resposta.status_code}')
    except requests.exceptions.RequestException:
        print(f'{Fore.RED}O site está morto!')

esta_online('https://www.ncousbocgso.com')