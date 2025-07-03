valor = input('Digite algo: ')

print(f'O valor digitado é: {type(valor)}')
print(f'É númerico? {valor.isnumeric()}')
print(f'É um texto? {valor.isalpha()}')
print(f'É alfanumérico? {valor.isalnum()}')
print(f'É maiúsculo? {valor.isupper()}')