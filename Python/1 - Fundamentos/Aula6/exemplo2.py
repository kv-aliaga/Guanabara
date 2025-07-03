# TESTE COM FLOAT
val1 = float(input('Digite um valor: '))

print(val1) # se digitar 5, vai mostrar 5.0, porque transforma em decimal

# TESTE COM BOOLEAN
val1 = bool(input('Digite um valor: '))

print(val1) # se digitar 5, vai mostrar True, porque val1 está preenchida

# SABER IDENTIFICAR VALORES
val2 = input('Digite outro valor: ')
print(val2.isnumeric())
print(val2.isalpha())
print(val2.isalnum())