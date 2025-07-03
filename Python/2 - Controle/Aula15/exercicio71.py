valorSaque = int(input('Digite o valor a ser sacado: R$'))

cedulas50 = valorSaque // 50
valorSaque %= 50

cedulas20 = valorSaque // 20
valorSaque %= 20

cedulas10 = valorSaque // 10
valorSaque %= 10

cedulas1 = valorSaque

print('\nRESULTADOS')
print(f'Cédulas de R$50: {cedulas50}')
print(f'Cédulas de R$20: {cedulas20}')
print(f'Cédulas de R$10: {cedulas10}')
print(f'Cédulas de R$1: {cedulas1}')