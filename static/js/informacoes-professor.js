var botao_dados = document.querySelector('#botao1')
var botao_diario = document.querySelector('#botao2')
var botao_frequencia = document.querySelector('#botao3')
var bloco_informacoes = document.querySelector('.parte_baixo')
var bloco_diario = document.querySelector('.diario')
var bloco_frequencia = document.querySelector('.frequencia')

function dados() {
    botao_dados.style['background-color'] = '#9d9d9d'
    botao_diario.style['background-color'] = 'buttonface'
    botao_frequencia.style['background-color'] = 'buttonface'
    bloco_informacoes.style.display = 'block'
    bloco_diario.style.display = 'none'
    bloco_frequencia.style.display = 'none'

}

function diario() {
    botao_dados.style['background-color'] = 'buttonface'
    botao_frequencia.style['background-color'] = 'buttonface'
    botao_diario.style['background-color'] = '#9d9d9d'
    bloco_informacoes.style.display = 'none'
    bloco_diario.style.display = 'block'
    bloco_frequencia.style.display = 'none'
}

function frequencia() {
    botao_dados.style['background-color'] = 'buttonface'
    botao_frequencia.style['background-color'] = '#9d9d9d'
    botao_diario.style['background-color'] = 'buttonface'
    bloco_informacoes.style.display = 'none'
    bloco_diario.style.display = 'none'
    bloco_frequencia.style.display = 'block'
}