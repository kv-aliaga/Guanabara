def notas(* notas):
    maior = media = total = 0
    menor = 10
    resultado = []
    for nota in notas:
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota
        total += nota
    media = total / (len(notas))
    resultado.append(maior)
    resultado.append(menor)
    resultado.append(media)
    resultado.append(len(notas))
    return resultado

ns = [10, 9.5, 8, 7, 10]
print(notas(* ns))
# ordem: maior, menor, media, qtdNotas