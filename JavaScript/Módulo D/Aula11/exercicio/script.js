var resultado = document.getElementById('resultado')
var pais = document.getElementById('pais')

resultado.style.height = '350px'
resultado.style.padding = '15px'

function mostraResultado(){
    if (pais.value == 'Brasil'){
        resultado.style.background = 'green'
        resultado.innerHTML = '<p>Você é Brasileiro!<br>Bem vindo ao Brasil!</p><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Flag_of_Brazil.svg/960px-Flag_of_Brazil.svg.png" height="250px">'
    } else {
        resultado.style.background = 'blue'
        resultado.innerHTML = '<p>Você é Estrangeiro!<br>Bem vindo ao Brasil!</p><img src="https://s2.glbimg.com/7i1DFuNfUKWCd98OjrIB_izax0c=/e.glbimg.com/og/ed/f/original/2015/05/22/bandeira.jpg" height="250px">'
    }
}