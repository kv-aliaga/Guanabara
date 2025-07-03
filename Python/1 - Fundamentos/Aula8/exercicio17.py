import math

catetoOp = float(input('Digite o valor do cateto oposto: '))
catetoAd = float(input('Digite o valor do cateto adjascente: '))

quadHipotenusa = math.pow(catetoAd, 2) + math.pow(catetoOp, 2)

print(f'A hipotenusa é igual a {math.sqrt(quadHipotenusa)}m')