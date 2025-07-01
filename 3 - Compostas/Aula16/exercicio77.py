palavras = ('Jones', 'Pedrao', 'Papelote')
vogais = ('a', 'e', 'i', 'o', 'u')
cont = contPalavra = 0

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} as vogais são:', end=' ')
    for letra in palavra:
        if letra.lower() in vogais:
            print(letra.lower(), end=' ')