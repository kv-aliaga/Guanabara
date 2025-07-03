extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um valor de 0 a 20 para ser convertido em extenso: '))
while True:
    if n < 0 or n > 20:
        print('O número precisa estar entre 0 e 20')
        n = int(input('Digite um valor de 0 a 20 para ser convertido em extenso: '))
    else:
        print(f'O número {n} em extenso é {extenso[n]}')
        continuar = input('Quer continuar? (S/N) ').upper()
        if continuar[0] == 'N':
            break
        else:
            n = int(input('\nDigite um valor de 0 a 20 para ser convertido em extenso: '))