function multiplicar(){
    // mesmo que estejam declarados como number no html, aqui eles são tratados como texto
    var tn1 = document.getElementById('txtn1')
    var tn2 = document.getElementById('txtn2')
    var res = document.getElementById('res')

    // Caso não fosse transformado em número, iria concatenar
    var n1 = Number(tn1.value)
    var n2 = Number(tn2.value)
    var s = n1 * n2

    res.innerHTML = `A multiplicação entre ${n1} e ${n2} é = ${s}`
}