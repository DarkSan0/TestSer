var botao_dados = document.querySelector('#botao1')
var botao_boletim = document.querySelector('#botao2')
var bloco_informacoes = document.querySelector('.parte_baixo')
var bloco_boletim = document.querySelector('.boletim')

function apagar_boletim() {
    botao_dados.style['background-color'] = '#9d9d9d'
    botao_boletim.style['background-color'] = 'buttonface'
    bloco_informacoes.style.display = 'block'
    bloco_boletim.style.display = 'none'

}

function apagar_dados() {
    botao_dados.style['background-color'] = 'buttonface'
    botao_boletim.style['background-color'] = '#9d9d9d'
    bloco_informacoes.style.display = 'none'
    bloco_boletim.style.display = 'flex'
}