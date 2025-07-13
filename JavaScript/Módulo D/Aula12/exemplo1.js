// CONDIÇÕES ANINHADAS
var idade = 85
if (idade < 16){
    console.log('Não vota')
} else{
    if (idade < 18 || idade > 80){
        console.log('Voto opcional')
    } else{
        console.log('Voto obrigatório')
    }
}

// USANDO ELSE IF
if (idade < 16){
    console.log('Não vota')
} else if (idade < 18 || idade > 80){
    console.log('Voto opcional')
} else{
    console.log('Voto obrigatório')
}