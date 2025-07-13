function calcular(){
    var txtv = document.getElementById('txtvel')
    var res = document.getElementById('res')
    var vel = Number(txtv.value)

    res.innerHTML = `Sua velocidade atual é de <strong>${vel}</strong>Km/h`
    if (vel > 60){
        res.innerHTML = '<style>#res{color: red;}</style>Voce está <strong>MULTADO!</strong> Por excesso de velocidade'
    } else{
        res.innerHTML = 'Siga seu caminho!'
    }
}