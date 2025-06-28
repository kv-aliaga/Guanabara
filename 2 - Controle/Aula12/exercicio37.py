from colorama import init, Fore
init(autoreset = True)

numero = int(input('Digite um número: '))

print(f"""{Fore.YELLOW}Escolha a forma de conversão do número {numero}
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL""")
escolha = int(input())

if (escolha == 1):
    numero = bin(numero)
elif (escolha == 2):
    numero = oct(numero)
else:
    numero = hex(numero)

print(Fore.GREEN + f'O resultado é: {numero}')