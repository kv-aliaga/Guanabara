teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:]) # não deixar só (teste) no append porque senão cria conexão entre listas

teste[0] = 'Maria'
teste[1] = 22

galera.append(teste[:]) # por mais que não parceça, agora galera mostrará [['Gustavo', 40], ['Maria', 41]]

print(galera)