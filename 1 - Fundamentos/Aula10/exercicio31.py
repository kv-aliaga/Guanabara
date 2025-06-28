distancia = float(input('Digite a distância da sua viagem de ônibus: '))

if (distancia <= 200):
    preco = distancia * 0.5
else:
    preco = distancia * 0.45

print(f'O total pago é de R${preco}')