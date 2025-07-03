frase = input('Digite uma frase: ')
frase = frase.lower()

print(f'Na frase aparecem {frase.count('a')} vezes a letra A')
print(f'Na frase ela aparece pela primeira vez no {frase.find('a')  + 1}º caractere')
print(f'Na frase ela aparece pela última vez no {frase.rfind('a') + 1}º caractere')