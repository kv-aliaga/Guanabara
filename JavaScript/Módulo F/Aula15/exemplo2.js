
let numeros = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco']

for (var i = 0; i < numeros.length; i ++){
    console.log(`A posição ${i} recebe ${numeros[i]}`)
}

// para cada posição na variavel composta mostra o valor na posição
for (let j in numeros){
    console.log(numeros[j])
}