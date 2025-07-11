// Document Object Model (DOM)

// ARVORE DOM                     
// WINDOW > DOCUMENT > HTML > HEAD > META, TITLE
//                          > BODY > P, H1, DIV

// para acessar:
window.document.writeln(window.document.URL)
document.writeln()

// TIPOS DE ACESSO

// por marca
// cria variavel, aciona ela, e nos parenteses onde ela vai performar e em qual vai ser (0 para o primeiro, 1 para o segundo...)
var novoTexto = window.document.getElementsByTagName('p')[0]
window.document.writeln('<br><br>Está escrio assim no primeiro parágrafo: ' + novoTexto.innerHTML)

var corpo = window.document.body
corpo.style.background = 'green'

var p2 = document.getElementsByTagName('p')[1]
document.writeln(p2.innerText) // Sem elementos da marcação HTML (exemplo: strong)
document.writeln(p2.innerHTML) // Com a marcação