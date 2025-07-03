from colorama import init, Fore, Back, Style

# Inicializa o Colorama e faz com que após cada print o texto resete
init(autoreset = True)

# Texto com diferentes cores
print(Fore.RED + 'Texto em vermelho')
print(Fore.GREEN + 'Texto em verde')
print(Fore.BLUE + 'Texto em azul')
print(Fore.YELLOW + 'Texto em amarelo')

# Fundo colorido
print(Back.RED + 'Fundo vermelho')
print(Back.CYAN + Fore.BLACK + 'Fundo ciano com texto preto')

# Estilos
print(Style.BRIGHT + 'Texto em negrito (BRIGHT)')
print(Style.DIM + 'Texto apagado (DIM)')
print(Style.NORMAL + 'Texto normal')

# Combinando tudo
print(Fore.WHITE + Back.MAGENTA + Style.BRIGHT + 'Texto branco, fundo magenta e brilhante')