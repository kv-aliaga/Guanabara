# entrada de dados
largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))

# análise de dados
area = largura * altura

# saída de dados
print(f'Para pintar {area}m² de parede são necessários {area / 2} litros de tinta')