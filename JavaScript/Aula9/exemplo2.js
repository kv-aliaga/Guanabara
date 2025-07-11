// SELEÇÃO POR ID
var clica = window.document.getElementById('clica')
clica.style.background = 'blue'
clica.innerHTML = '<strong>ESTOU ESPERANDO...</strong>'

// SELEÇÃO POR NOME
clica = window.document.getElementsByName('clica')[0]
clica.style.background = 'yellow'
clica.innerHTML = '<strong>ESTOU ESPERANDO...</strong>'

// SELEÇÃO POR SELETOR
var d = window.document.querySelector('div#clica')
d.style.background = 'orange'