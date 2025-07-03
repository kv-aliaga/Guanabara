from colorama import init, Fore
init(autoreset=True)

preco = float(input('Digite o preço do produto: '))

print(f"""Forma de pagamento:
{Fore.CYAN}[1]{Fore.RESET} Dinheiro / Cheque
{Fore.CYAN}[2]{Fore.RESET} Cartão""")
opcao = int(input())

juros = 0
parcelas = 1

if opcao == 1:
    preco_final = preco * 0.9
    info_extra = f"DESCONTO: {Fore.GREEN}R${preco - preco_final:.2f}"
else:
    print(f"""Opção no cartão:
    {Fore.CYAN}[1]{Fore.RESET} À vista (10% de desconto)
    {Fore.CYAN}[2]{Fore.RESET} 2x sem juros (5% de desconto)
    {Fore.CYAN}[3]{Fore.RESET} 3x ou mais (pelo menos 30% de juros)""")
    tipo = int(input())

    if tipo == 1:
        preco_final = preco * 0.9
        info_extra = f"DESCONTO: {Fore.GREEN}R${preco - preco_final:.2f}"
    elif tipo == 2:
        preco_final = preco * 0.95
        parcelas = 2
        info_extra = f"DESCONTO: {Fore.GREEN}R${preco - preco_final:.2f}"
    else:
        parcelas = int(input('Quantas parcelas? '))
        juros = parcelas / 10
        preco_final = preco * (1+juros)
        info_extra = f"JUROS: {Fore.RED}R${preco_final - preco:.2f}"

print('\nVALORES FINAIS')
print(f'PREÇO NORMAL: R${preco:.2f}')
print(info_extra)
print(f'PREÇO FINAL: {Fore.BLUE}R${preco_final:.2f}')
if parcelas > 1:
    print(f'PARCELADO EM {parcelas}x DE R${preco_final/parcelas:.2f}')