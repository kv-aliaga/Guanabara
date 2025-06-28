tempo = int(input('Digite quantos anos você tem seu carro: '))

# modelo comum
if (tempo <= 3):
    print('Carro novo')
else:
    print('Carro velho')

# modelo simplificado
print('Carro novo' if tempo <= 3 else 'Carro velho')