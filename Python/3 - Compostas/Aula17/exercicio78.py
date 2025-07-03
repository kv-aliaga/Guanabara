maior = posMaior = posMenor = 0
menor = 999 * pow(999, 3)
numeros = []

for i in range(0, 5):
    num = int(input(f'Digite o {i + 1}º valor da lista: '))
    numeros.append(num)
    
    if numeros[i] > maior:
        maior = numeros[i]
        posMaior = i
    if numeros[i] < menor:
        menor = numeros[i]
        posMenor = i

print('\nRESULTADS FINAIS')
print(f'Maior número: {maior}, posição: {posMaior}')
print(f'Menor número: {menor}, posição: {posMenor}')