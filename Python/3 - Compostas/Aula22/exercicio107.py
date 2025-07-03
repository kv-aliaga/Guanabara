from uteis.numeros.moeda import aumentar, dobro, metade
from uteis.numeros.moeda import moeda

num1 = float(input('Digite o preço: R$'))

print(f'A metade de {moeda(num1)} é {metade(num1, 'N')}')
print(f'O dobro de {moeda(num1)} é {(dobro(num1))}')
print(f'Aumentando 10% de {moeda(num1)}; temos {(aumentar(num1, 10))}')