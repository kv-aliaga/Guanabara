def maior(* numero):
    maior = 0
    for n in numero:
        if n > maior:
            maior = n
    
    print(f'Foram analisados {len(numero)} números')
    print(f'O maior número é {maior}')

maior(1, 2, 3, 4, 5, 6, 7, 8, 9)