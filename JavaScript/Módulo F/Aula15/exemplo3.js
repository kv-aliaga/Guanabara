let numeros = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco']

console.log(numeros.indexOf('dois')) // retorna 2
console.log(numeros.indexOf('seis')) // retorna -1, porque não existe em numeros

numeros.sort()

console.log(numeros.indexOf('dois')) // retorna 1, por causa do sort

let posicao = numeros.indexOf('dez')
console.log(posicao == -1 ? 'O valor não foi encontrado': `O valor está na posição ${numeros[posicao]}`)