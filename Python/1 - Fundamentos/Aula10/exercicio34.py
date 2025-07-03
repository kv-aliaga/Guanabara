salario = float(input('Digite o valor do salário: '))

if (salario > 1250):
    salario += salario * 0.1
else:
    salario += salario * 0.15
print(f'O salário final é de: R${salario}')