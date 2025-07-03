from colorama import init, Fore
init(autoreset = True)

# Variaveis de cores

valorCasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salário do comprador: '))
qtdAnos = int(input('Digite a quantidade de anos a serem pagos: '))

qtdMeses = qtdAnos * 12
parcelas = valorCasa / qtdMeses

if (parcelas > salario * 0.3):
    print(Fore.RED + 'Empréstimo negado')
else:
    print(Fore.GREEN + 'Empréstimo aceito!')
print(f'Parcelas de: {Fore.YELLOW}R${parcelas :.2f}')