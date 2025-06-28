# conta de 1 a 5
for i in range (1, 6): 
    print(i)

print()

# conta de 5 a 1
for i in range (5, 0, -1):
    print(i)

print()

# conta de 5 a 1 pulando 2 números
for i in range (5, 0, -2):
    print(i)

print()

# range com input parcial (de 1 a n)
n = int(input('Digite o número final da contagem: '))
for i in range (1, (n + 1)):
    print(i)

# range com input total (de m a n pulando p números)
m = int(input('Digite o número inicial da contagem: '))
n = int(input('Digite o número final da contagem: '))
p = int(input('Digite quantos números serão pulados (se não quiser, digite 1): '))

for i in range(m, (n + 1), p):
    print(i)

# usos do for
total = 0
for i in range(0, 5):
    n = int(input('Digite um número: ')) # pergunta 5 vezes
    total += n
print(f'O total é: {total}')