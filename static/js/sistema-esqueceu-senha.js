const matriculaFixa = '20221461'; // Matrícula fixa
const nomeFixo = 'David'; // Nome fixo
const emailFixo = 'monohtoplane@gmail.com'; // Email fixo

const form = document.getElementById('formulario');
form.addEventListener('submit', function (event) {
    event.preventDefault();

    const matricula = document.getElementById('matricula').value;
    const nome = document.getElementById('nome').value;

    if (matricula === matriculaFixa && nome === nomeFixo) {
        alert('Email enviado com sucesso');
    } else {
        alert('Sua matricula ou seu nome não Consta no sistema!');
    }
});

function exibirMensagem(mensagem) {
    const mensagemElement = document.createElement('p');
    mensagemElement.textContent = mensagem;
    document.body.appendChild(mensagemElement);
}