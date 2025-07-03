# Falha Sintática
#   erro de escrita no código (ex.: primt(x))

# Exceção
#   erro de digitação no terminal (ex.: 10 / 'jones')

try: # tenta achar o erro
    a = float(input('numerador: '))
    b = float(input('donminador: '))
    
    r = a / b
    

#       sempre com aspas
except (ValueError, TypeError): # se mostrar o erro
    print('Houve um problema com o tipo de dado')
except ZeroDivisionError:
    print('Não é possível dividir por zero')
except KeyboardInterrupt:
    print('Digite os dados')
else: # senão
    print(f'O resultado é {r:.2f}')
finally: # mostrar independente de certo ou errado
    print('Volte sempre!')