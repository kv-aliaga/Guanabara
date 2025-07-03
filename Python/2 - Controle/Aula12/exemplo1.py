idade = int(input('Digite sua idade: '))

if (idade <= 10):
    print('Classe infantil')
elif (idade <= 16):
    print('Classe adolescente')
elif (idade <= 25):
    print('Classe jovem')
else:
    print('Classe adulta')