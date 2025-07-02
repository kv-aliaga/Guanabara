continuar = 0
boletim = list()

while True:
    nome = input('\nNome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    
    boletim.append([nome, [nota1, nota2], media])
    
    cont = input('Continuar? [S/N]: ')
    if cont in 'Nn':
        break

print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)

for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-='*30)
    opc = int(input('Mostrar notas de qual aluno? (999 para): '))
    if opc == 999:
        break
    if opc <= len(boletim) - 1:
        print(f'Notas de {boletim[opc][0]} são {boletim[opc][1]}')