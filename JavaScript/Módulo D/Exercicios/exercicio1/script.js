function carregar(){
    var msg = document.getElementById('msg')
    var img = document.getElementById('img')
    var area = document.getElementById('area')

    var data = new Date()
    var hora = data.getHours()

    msg.innerHTML = `Agora são ${hora} horas`

    if (hora >= 0 && hora < 12){
        img.src = 'Images/natu.png'
        area.style.background = '#89C757'
    } else if (hora >= 12 && hora < 18){
        img.src = 'Images/torkoal.png'
        area.style.background = '#EE9E74'
    } else{
        img.src = 'Images/munna.png'
        area.style.background = '#AA85B6'
    }
}