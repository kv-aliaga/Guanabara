def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print('\033[31mErro! Digite um número inteiro válido.\033[m')

def leiaFloat(msg):
    while True:
        try:
            valor = float(input(msg))
            return valor
        except ValueError:
            print('\033[31mErro! Digite um número real válido.\033[m')

n1 = leiaInt('Inteiro: ')
n2 = leiaFloat('Decimal: ')