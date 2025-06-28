idades = 0
homemMaisVelho = ''
idadeHomemMaisVelho = 0
contMulheresMenor20 = 0
for i in range (1, 5):
    print()
    nome = input('Digite o nome: ')
    idade = int(input('Digite sua idade: '))
    genero = input('Digite seu gênero (M / F): ').lower()
    idades += idade
    
    if (genero == 'M'.lower() and idade > idadeHomemMaisVelho):
        homemMaisVelho = nome
    if (genero == 'F'.lower() and idade < 20):
        contMulheresMenor20 += 1

print(f'\nMédia de idade do grupo: {idades / 4}')
print(f'Nome do homem mais velho: {homemMaisVelho}')
print(f'Quantidade de mulheres com menos de 20 anos: {contMulheresMenor20}')