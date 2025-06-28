nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if (media < 4):
    print('Estude mais')
elif (media < 6):
    print('Quase consegiu')
else:
    print('Parabéns!')