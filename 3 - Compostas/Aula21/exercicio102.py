def fatorial(numero, show = 'N'):
    """Faz o fatorial de um número inteiro e opcionalmente mostra o processo

    Args:
        numero (int): número inteiro a ser colocado
        show (str, optional): escolha se vai ver (qualquer valor) ou não ('N'). Defaults to 'N'.

    Returns:
        int: total do fatorial
        exemplo: 5 -> 120
        
    Feito por Davi Aliaga @kv-aliaga
    """
    f = 1
    if show == 'N':
        for i in range(numero, 0, -1):
            f *= i
    else:
        for i in range(numero, 1, -1):
            f *= i
            print(f'{f} * {i-1} = {f*(i-1)}')
    return f

n = int(input('Número: '))
ver = (input('Ver processo? (S/N): ')).upper()
print(f'O total foi de {fatorial(n, ver)}')