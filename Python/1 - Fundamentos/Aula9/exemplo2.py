frase = 'Meu nome é Kavhsao'

print(len(frase))# mostra quantos caracteres a frase tem
print(frase.count('e')) # conta quantas vezes tem o caractere 'e'
print(frase.count('e', 0,15)) # conta quantas vezes temm o carcatere 'e' do 1º ao 15º caracteres
print(frase.find('me')) # mostra na cadeia de caracteres onde começou a última vez que essa sequência aparece
print(frase.find('Jones')) # aparece -1, já que não existe
print('Jones' in frase) # aparece False
print(frase.replace('Kavhsao', 'Jones')) # substitui temporariamente Kavhsao por Jones
print(frase.upper()) # deixa texto em maiúsculo
print(frase.lower()) # deixa texto em minúsculo
print(frase.capitalize()) # deixa primeiro caractere em maiúsculo
print(frase.title()) # após cada espaço, deixa o primeiro caractere em maiúsculo