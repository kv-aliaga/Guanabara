function calcular(){
    var n = Number(document.getElementById('n').value)
    var resultado = document.getElementById('resultado')

    for (var c = 1; c <= 10; c ++){
        if (n == 0){
            break
        }
        resultado.innerText += `${n} * ${c} = ${n*c}\n`
        resultado.style.textAlign = 'center'
    }
}