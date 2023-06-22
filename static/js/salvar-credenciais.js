// Função para salvar as credenciais no "lembre de mim"
function salvarCredenciais() {
    var matricula = document.getElementById("username").value; // Obtém o valor do campo de matrícula
    //var senha = document.getElementById("password").value; // Obtém o valor do campo de senha
    var lembrar = document.getElementById("lembrar").checked; // Obtém o valor da caixa de seleção "lembrar"

    if (lembrar) {
        // Se a caixa de seleção "lembrar" estiver marcada armazena a matrícula e a senha no localStorage
        localStorage.setItem("username", matricula);
        //localStorage.setItem("password", senha);
    } else {
        // Se a caixa de seleção "lembrar" não estiver marcada remove a matrícula e a senha do localStorage
        localStorage.removeItem("username");
        //localStorage.removeItem("password");
    }
}

// Função para preencher as credenciais salvas
function preencherCredenciaisSalvas() {
    // Obtém a matrícula e a senha salva do localStorage
    var matriculaSalva = localStorage.getItem("username");
    // var senhaSalva = localStorage.getItem("password");
    if (matriculaSalva && senhaSalva) {
        // Se a matrícula e senha salvas existirem
        document.getElementById("username").value = matriculaSalva; // Preenche o campo de matrícula com o valor salvo
        // document.getElementById("password").value = senhaSalva; // Preenche o campo de senha com o valor salvo
        document.getElementById("lembrar").checked = true; // Marca a caixa de seleção "lembrar"
    }
}

// Chama a função ao carregar a página
preencherCredenciaisSalvas();

