function calcular(){
    var n = Number(document.getElementById('n').value)
    var resultado = document.getElementById('resultado')

    resultado.innerText = 'Tabuada:\n'

    for (var c = 1; c <= 10; c ++){
        if (n == 0){
            break
        }
        resultado.innerText += `${n.toFixed(2)} * ${c} = ${(n*c).toFixed(2)}\n`
        resultado.style.textAlign = 'center'
    }
}