function contar(){
    var inicio = Number(document.getElementById('i').value)
    var fim = Number(document.getElementById('f').value)
    var passo = Number(document.getElementById('p').value)
    var resultado = document.getElementById('resultado')

    resultado.innerText = 'Contando:\n'

    if (passo <= 0){
        passo = 1
    }
    for (inicio; inicio <= fim; inicio += passo){
        if (inicio == 0){
            resultado.innerText += ''
        } else if (inicio < (fim - passo)){
            resultado.innerText += `${inicio}, `
        } else{
            if (inicio < (fim - passo)){
                resultado.innerText += `${inicio},${fim}`
            } else{
                resultado.innerText += `${inicio}`
            }
        }
    }
}