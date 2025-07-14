// repetições

//function comerPizza(){
//    while (temFatia()){ <- enquanto tiverem fatias de pizza ele come
//        comerFatia()
//    }
//}

// teste lógico (while) no início
var cont = 1
while (cont < 6){
    console.log(`Passo ${cont}`)
    cont ++
}
cont = 0

// teste lógico (while) no fim
do {
    console.log(`${cont}`)
    cont ++
} while (cont < 6)