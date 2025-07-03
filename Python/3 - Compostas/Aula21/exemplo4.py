# ESCOPO DE VARIÁVEIS
def teste():
    x = 8 # variável local
    print(f'Na função teset, x = {x}') # 8
    print(f'Na função teste, n = {n}') # 2

n = 2 # variável global
print(f'No programa principal, n = {n}') # 2
print(f'No programa principal, x não existe') # x = {x} não funcionaria porque essa variável só existe dentro de teste()

# duas variáveis 'iguais' podem existir ao mesmo tempo
def teste2(a):
    a = 8
    print(f'\na, na função teste2 vale: {a}') 

a = 2
teste2(a)
print(f'a, no global vale: {a}')

# resolvendo a situação acima
def teste2():
    global a # pede para o computadoor que ao invés de criar uma variável local dentro do escopo de teste2 para a, use o espaço da memória salvo globalmente, ou seja a partir da próxima linha, independente de tudo, a = 8
    a = 8
    print(f'\na, na função teste2 vale: {a}') 

a = 2
teste2()
print(f'a, no global vale: {a}')