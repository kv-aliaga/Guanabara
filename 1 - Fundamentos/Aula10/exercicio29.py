velocidade = float(input('Digite a velocidade do carro em km/h: '))

if (velocidade <= 80):
    print('Velocidade dentro dos limites')
else:
    excedido = velocidade - 80
    excedido *= 7
    print(f'Valor da multa R${excedido}')