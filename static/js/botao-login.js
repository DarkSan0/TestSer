// Verificar se todos os campos estão preenchidos
function checkInputs() {
    const matricula = document.getElementById('username'); // Obtém o elemento de entrada de matrícula
    const senha = document.getElementById('password'); // Obtém o elemento de entrada de senha
    const submitButton = document.querySelector('#loginForm button[type="submit"]'); // Obtém o botão de envio

    if (matricula.value.trim() !== '' && senha.value.trim() !== '') {
        // Verifica se os campos de matrícula e senha não estão vazios após remover os espaços em branco
        submitButton.removeAttribute('disabled'); // Remove o atributo 'disabled' do botão de envio
    } else {
        submitButton.setAttribute('disabled', 'disabled'); // Define o atributo 'disabled' no botão de envio
    }
}

// Adicionar ouvintes de evento aos campos de entrada
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');
usernameInput.addEventListener('input', checkInputs);
passwordInput.addEventListener('input', checkInputs);
