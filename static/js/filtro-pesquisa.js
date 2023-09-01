const INPUT_BUSCA = document.getElementById('input-buscar');
const TABELA = document.getElementById('tabela');

INPUT_BUSCA.addEventListener('keyup', () => {
    let expressao = INPUT_BUSCA.value.toLowerCase();

    let linhas = TABELA.getElementsByTagName('tr');

    for (let posicao in linhas) {
        if (true === isNaN(posicao)) {
            continue;
        }
            
        let conteudoDalinha = linhas[posicao].innerHTML.toLowerCase();

        if (true === conteudoDalinha.includes(expressao)) {
            linhas[posicao].style.display = '';
        } else {
            linhas[posicao].style.display = 'none';
        }
    }

})