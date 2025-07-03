# usando string
numero = input('Digite um número: ')

print(f'Unidade: {numero[3]}')
print(f'Dezena: {numero[2]}')
print(f'Centena: {numero[1]}')
print(f'Milhar: {numero[0]}')

print()

# usando cálculos
numero = int(numero)

print(f'Unidade: {(((numero % 1000) % 100) % 10) % 10}')
print(f'Dezena: {((numero // 10) % 100) % 10 }')
print(f'Centena: {(numero // 100) % 10}')
print(f'Milhar: {numero // 1000}')