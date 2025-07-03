from datetime import datetime
def voto(anoNascimento):
    idade = datetime.now().year - anoNascimento
    
    if idade < 18:
        return 'negado'
    elif idade < 71:
        return 'obrigatório'
    else:
        return 'opcional'

anoNasc = int(input('Ano de nascimento: '))
print(f'Tendo {datetime.now().year - anoNasc} anos, seu voto é {voto(anoNasc)}')