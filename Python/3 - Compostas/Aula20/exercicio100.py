from random import sample

def sorteia(* numero):
    sorteados = (sample(numero, k=5))
    print(f'Os números escolhidos foram: {sorteados}')
    return sorteados

def somaPar(* numero):
    somaPar = 0
    for n in numero:
        if n % 2 == 0:
            somaPar += n
    print(f'A soma dos número pares é: {somaPar}')

sorteados = sorteia(1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11, 12, 13, 14, 15)
somaPar(* sorteados)