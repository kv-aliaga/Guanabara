var nome = window.prompt('Digite seu nome')

const p = document.createElement('p')
p.innerText = `O nome ${nome} tem ${nome.length} letras`

document.body.appendChild(p);