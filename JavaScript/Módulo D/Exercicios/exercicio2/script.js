function verificar(){
    var anoNacimento = Number(document.getElementById('anonasc').value)
    var genero = document.querySelector('input[name="genero"]:checked').value
    var foto = document.getElementById('foto')
    var resultado = document.getElementById('r')
    var agora = new Date()
    var ano = agora.getFullYear()
    var idade = ano - anoNacimento

    if (idade <= 0){
        resultado.innerText = `Detectamos um espermatozoide que nascerá em ${idade * -1} anos.`
        foto.src = 'Images/espermatozoide.png'
    }else if (idade > 123 && idade != ano){
        resultado.innerText = `Detectamos um esqueleto que morreu há ${idade - 75} anos.`
        foto.src = 'Images/esqueleto.png'
    } else if (genero == 'masculino'){
        resultado.innerText = `Detectamos um homem de ${idade} anos.`
        if (idade < 5){
            foto.src = 'Images/homens/bebe_menino.png'
        } else if (idade < 12){
            foto.src = 'Images/homens/crianca_menino.png'
        } else if (idade < 20){
            foto.src = 'Images/homens/adolescente_menino.png'
        } else if (idade < 59){
            foto.src = 'Images/homens/adulto_menino.png'
        } else{
            foto.src = 'Images/homens/idoso_menino.png'
        }
    } else if (genero == 'feminino'){
        resultado.innerText = `Detectamos uma mulher de ${idade} anos.`
        if (idade < 5){
            foto.src = 'Images/mulheres/bebe_menina.png'
        } else if (idade < 12){
            foto.src = 'Images/mulheres/crianca_menina.png'
        } else if (idade < 20){
            foto.src = 'Images/mulheres/adolescente_menina.png'
        } else if (idade < 59){
            foto.src = 'Images/mulheres/adulta_menina.png'
        } else{
            foto.src = 'Images/mulheres/idosa_menina.png'
        }
    }
}