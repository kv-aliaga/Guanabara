from colorama import init, Fore
init(autoreset = True)

nota1 = float(input('Digite a primera nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))

media = (nota1 + nota2) / 2

if (media < 5):
    print(f'{Fore.RED}Média: {media}\nReprovado')
elif (media < 7):
    print(f'{Fore.YELLOW}Média: {media}\nRecuperação')
else:
    print(f'{Fore.GREEN}Média: {media}\nAprovado')