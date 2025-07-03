nomeComp = input('Digite seu nome completo: ')

print(f'Nome em maiúsculo: {nomeComp.upper()}')
print(f'Nome em minúsculo: {nomeComp.lower()}')
print(f'Quantidade de caracteres sem considerar espaço: {len(nomeComp.replace(' ', ''))}')
print(f'Quantidade de caracteres do primeiro nome: {len(nomeComp.split()[0])}')