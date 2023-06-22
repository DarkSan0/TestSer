// Verificar os eventos de input nos campos
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');
usernameInput.addEventListener('input', checkInputs);
passwordInput.addEventListener('input', checkInputs);

// Verificar o formulário de login ao ser enviado
const loginForm = document.getElementById('loginForm');
loginForm.addEventListener('submit', function (event) {
    event.preventDefault(); // Evita o envio padrão do formulário

    const username = document.getElementById('username');
    const password = document.getElementById('password');
    const errorMessage = document.getElementById('errorMessage');

    // Verifica as credenciais
    if (username.value === 'aluno' && password.value === '1234') {
    // Login bem-sucedido
    errorMessage.textContent = ''; // Limpa a mensagem de erro
    loginForm.submit(); // Envio do formulário
    } else {
    // Login inválido
    errorMessage.textContent = 'Matrícula ou senha incorretas.';
    }
});