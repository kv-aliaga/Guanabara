from datetime import datetime

cont = 0
for i in range (1, 8):
    ano = int(input('Digite o ano que você nasceu: '))
    idade = datetime.now().year - ano
    if (idade < 18):
        cont += 1
print(f'Pessoas que atingiram a maioridade: {7 - cont}')
print(f'Pessoas que não atingiram a maioridade: {cont}')