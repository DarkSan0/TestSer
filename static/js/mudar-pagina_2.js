let paginaAtual = 1; // Define a página ativa inicial
        
function mudarPagina(pagina) {
    if (pagina < 1 || pagina > 2) {
        return; // Não permitir ir além dos limites de página
    }
    
    // Esconde o conteúdo da página atual
    document.getElementById(`page${paginaAtual}`).style.display = 'none';
    
    // Mostra o conteúdo da nova página
    document.getElementById(`page${pagina}`).style.display = 'block';
    
    // Atualiza a classe ativa para a página atual e a nova página
    document.querySelectorAll('.pagination_section a').forEach((link, index) => {
        if (index + 1 === paginaAtual) {
            link.classList.remove('active');
        } else if (index + 1 === pagina) {
            link.classList.add('active');
        }
    });
    
    paginaAtual = pagina;
}