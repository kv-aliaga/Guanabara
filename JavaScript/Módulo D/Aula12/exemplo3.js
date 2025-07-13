// CONDIÇÃO MÚLTIPLICA (sempre usar break no final de cada case!!!!)
// Só funciona com números inteiros e caracteres, sem operadores

var agora = new Date()
var diaDaSemana = agora.getDay()

switch (diaDaSemana){
    case 0:
        console.log('Domingo')
        break
    case 1:
        console.log('Segunda-Feira')
        break
    case 2:
        console.log('Terça-Feira')
        break
    case 3:
        console.log('Quarta-Feira')
        break
    case 4:
        console.log('Quinta-Feira')
        break
    case 5:
        console.log('Sexta-Feira')
        break
    case 6:
        console.log('Sábado')
        break
    default:
        console.log('Erro')
}

// Sem break, caso diaDaSemana fosse 5 apareceria:
// Sexta-Feira
// Sábado
// Erro