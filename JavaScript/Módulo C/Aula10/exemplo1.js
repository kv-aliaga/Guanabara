// EVENTOS: exemplos
// Quando o mouse entra na área da div: mouseenter
// Quando o mouse se mexe na área da div: mousemove
// Quando o mouse clica e segura na área da div: mousedown
// Quando solta: mouseup
// Quando clica: click

// FUNÇÕES: códigos acionados quando um evento acontece
// function ação(parametros){}
var area = document.getElementById('area')

// cria checadores automático de eventos para não poluir o html
area.addEventListener('click', clicar);
area.addEventListener('mouseenter', entrar);
area.addEventListener('mouseout', sair);

function clicar(){
    area.innerHTML = '<strong>JavaScript</strong>'
    area.style.background = 'yellow'
    area.style.color = 'black'
}

function entrar(){
    area.innerHTML = '<strong>Entrou</strong>'
    area.style.background = 'blue'
}

function sair(){
    // Depois que sai, ele nunca mais volta ao original
    area.innerHTML = '<strong>Saiu</strong>'
    area.style.background = 'orange'
}

// Se após fazer o código JavaScript e perceber que houve um erro, o recomendado é abrir o HTML no navegador e, em inspecionar buscar os erros