from utils import *
from colorama import init, Fore
import os

init(autoreset=True)
acabou = False
caminho = r"C:\Users\kavhs\OneDrive\Desktop\Programação\Python\Guanabara\Guanabara\Python\3 - Compostas\Aula23\cadastro.txt"
pessoas = {}
resultado = []
inicio = 'PESSOAS CADASTRADAS'

if not os.path.exists(caminho):
    with open(caminho, 'w', encoding='utf8') as arquivo:
        arquivo.write(f'{lin(inicio)}\n')

while acabou == False:
    menu()
    try:
        escolha = int(input(f'{Fore.GREEN}Sua opção: {Fore.RESET}'))
        verificarMenu(escolha)
    except (ValueError, TypeError):
        print(f'{Fore.RED}\nDigite apenas números inteiros nos limites\n')
    except ValorForaLimite as vfl:
        print(vfl)
    else:
        if escolha == 0:
            print(f'{Fore.MAGENTA}Obrigado por usar!')
            break
        if escolha == 1:
            print()
            with open(caminho, 'r', encoding='utf8') as arquivo:
                for linha in arquivo:
                    linhaLimpa = linha.strip()
                    if linhaLimpa:
                        print(linhaLimpa)
            print()
        if escolha == 2:
            print(lin('NOVO CADASTRO'))
            while True:
                try:
                    nome = input('Nome: ')
                    idade = int(input('Idade: '))
                    verificarSobrenome(nome)
                    verificarIdade(idade)
                except (ValueError, TypeError):
                    print(f'\n{Fore.RED}Digite uma idade de número inteiro\n')
                except ValorForaLimite as vfl:
                    print(vfl)
                except SemSobrenome as ss:
                    print(ss)
                else:
                    pessoas['nome'] = nome
                    pessoas['idade'] = idade
                    
                    resultado.append(pessoas.copy())
                    
                    print(f'\n{Fore.YELLOW}Novo registro de {nome} adicionado\n')
                    
                    with open(caminho, 'a', encoding='utf8') as arquivo:
                        arquivo.write(f'\n{nome:<30}{idade:>15} anos')
                    break