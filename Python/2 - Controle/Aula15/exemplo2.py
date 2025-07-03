# exemplo de verificação sem while true
n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
s -= 999 # gambiarra
print(s)

n = s = 0
# verificação com while true
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(s)