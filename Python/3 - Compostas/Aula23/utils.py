from colorama import init, Fore
init(autoreset=True)

class ValorForaLimite(Exception):
    def __init__(self, valor, minimo, maximo):
        self.valor = valor
        self.minimo = minimo
        self.maximo = maximo
        super().__init__(f'\n{Fore.RED}Valor {valor} fora do intervalo permitido de {minimo} a {maximo}\n')

class SemSobrenome(Exception):
    def __init__(self, nome):
        self.nome = nome
        super().__init__(f'\n{Fore.RED}{nome} precisa ter um sobrenome registrado\n')

def verificarSobrenome(nome):
    qtdEspacos = nome.count(' ')
    if qtdEspacos == 0:
        raise SemSobrenome(nome)

def verificarMenu(valor):
    if not 0 <= valor <= 2:
        raise ValorForaLimite(valor, 0, 2)

def verificarIdade(valor):
    if not 0 <= valor <= 123:
        raise ValorForaLimite(valor, 0, 123)

def lin(texto):
    tamanho = (len(texto) * 3)
    linha = '-' * tamanho
    centro = f'{texto:^{tamanho}}'
    return f'{linha}\n{centro}\n{linha}'

def menu():    
    print(lin('MENU PRINCIPAL'))
    print(f'{Fore.YELLOW}1{Fore.RESET} - {Fore.BLUE}Ver pessoas cadastradas')
    print(f'{Fore.YELLOW}2{Fore.RESET} - {Fore.BLUE}Cadastrar novas pessoas')
    print(f'{Fore.YELLOW}0{Fore.RESET} - {Fore.BLUE}Sair do sistema')