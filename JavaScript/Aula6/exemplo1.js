// PARSE EM JS
var n1 = Number.parseFloat(window.prompt('Digite o primeiro número: ')) // não é necessário fazer a conversão usando .parseFloat ou .parseInt nas versões atuais. O prórpio JavaScript entende quais são os tipos dos números
var n2 = Number(window.prompt('Digite o segundo número: ')) // prompts sempre são para strings, se quiser fazer contas é preciso usar type cast

var s = n1 + n2 // sem type cast ficaria -> s = 4 + 2 == '42'
window.alert('A soma é ' + s)

String(n1) // para string