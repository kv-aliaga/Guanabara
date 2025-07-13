var numero = 2000
var valorReal = numero.toLocaleString('pt-br', {style: 'currency', currency: 'BRL'})

window.alert(`${numero} equivale a ${valorReal}`)