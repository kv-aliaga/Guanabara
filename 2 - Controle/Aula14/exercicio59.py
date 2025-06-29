num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo valor: '))
escolha = 0

while escolha != 5:
    print("""
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    """)
    escolha = int(input('Escolha uma opção: '))
    if escolha == 1:
        print(f'{num1} + {num2} = {num1 + num2}')
    elif escolha == 2:
        print(f'{num1} * {num2} = {num1 * num2}')
    elif escolha == 3:
        print('O maior número é: ', num1 if num1 > num2 else num2)
    elif  escolha == 4:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo valor: '))