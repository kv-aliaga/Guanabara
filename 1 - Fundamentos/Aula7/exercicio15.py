kmRodados = float(input('Digite quantos km foram percorridos: '))
dias = int(input('Digite por quantos dias o carro foi alugado: '))

kmRodados *= 0.15
dias *= 60

print(f'O total a ser pago é: R${kmRodados + dias}')