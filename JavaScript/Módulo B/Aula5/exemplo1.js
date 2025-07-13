// TRÊS FORMAS DE SE ESCREVER EM JAVASCRIPT
alert('Escrever com Aspas Simples') // para escrever algo
alert(`Escrever
        Com
        Crase`) // multilinha e comportamento semelhante a f-string
// REGRAS PARA MNOMEAR IDENTIFICADORES
//      só podem começar com letras $ ou _
//      possível usar números, acentos, símbolos (exceto no começo)
//      não podem conter espaços ou palavras reservadas (ex.: var jo nes;  var var)

// CRIANDO VARIAVEIS COM O NODE
// 'node' > 'var' > enter > '<nomevar> = <valor>'

// DESCOBRINDO TIPOS
// 'typeof <nomevar>' <- diferente de outras linguagens, no mesmo arquivo uma variável pode ser: number, string, boolean, ou undefined

var n1
typeof n1 // undefined
n1 = Infinity // number
n1 = 3.1415 // number
n1 = 9 // number
n1 = null // object
n1 = 'Jones' // string
n1 = true // boolean
n1 = undefined // undefined