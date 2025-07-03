idade = genero = escolha = 0
qtdMaiorIdade = qtdHomens = qtdMulheresMenor20 = 0
cont = 1

while True:
    idade = int(input(f'\nDigite a idade da {cont}º pessoa: '))
    genero = input(f'Digite o gênero da {cont}º pessoa (M/F): ').upper()
    escolha = input(f'Deseja continuar? (S/N): ').upper()

    if escolha[0] == 'N':
        break
    else:
        if idade > 18:
            qtdMaiorIdade += 1
        if genero[0] == 'M':
            qtdHomens += 1
        if genero[0] == 'F' and idade < 20:
            qtdMulheresMenor20 += 1
    cont += 1

print('\n\nResultados Finais: ')
print('Pessoas com mais de 18 anos: ', qtdMaiorIdade)
print('Quantidade de homens: ', qtdHomens)
print('Quantidade de mulheres com menos de 20 anos: ', qtdMulheresMenor20)