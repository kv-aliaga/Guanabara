let numeros = []

function adicionar(){
    var num = Number(document.getElementById('n').value)
    var adiciona = document.getElementById('add')

    if (num < 0 || num > 100){
        alert('Digite entre 1 e 100')
    } else{
        numeros.push(num)
        adiciona.innerText += `\nValor ${num} adicionado.`
    }
}

function finalizar(){
    var resultado = document.getElementById('r')
    var maior = Math.max(...numeros)
    var menor = Math.min(...numeros)
    var soma = 0
    var media = 0

    for (var num of numeros){
        soma += num
    }
    media = soma / numeros.length

    resultado.innerText = `Resultados:\n`

    resultado.innerText += `Ao todo, temos ${numeros.length} números cadastrados\n`
    resultado.innerText += `O maior valor informado foi ${maior}\n`
    resultado.innerText += `O menor valor informado foi ${menor}\n`
    resultado.innerText += `Somando todos os valores, temos ${soma}\n`
    resultado.innerText += `A média dos valores digitados é ${media.toFixed(2)} \n`   

}

function inicializar(){
    adicionar()
    finalizar()
}
