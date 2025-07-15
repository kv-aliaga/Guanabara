// Funções executadas quando chamadas em decorrencia de um evento
// Função pode ter parâmetros e retornar algo, geralmente no fim de operações

//function ação(parametro){
//    return resultado
//}

//ação(5) <- retorna resultado

function parOuImpar(numero){
    if (numero % 2 == 0){
        return 'par'
    } else{
        return 'ímpar'
    }
}

console.log(parOuImpar(15))