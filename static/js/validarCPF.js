function TestaCPF(strCPF) {
    var Soma;
    var Resto;
    Soma = 0;
  if (strCPF == "00000000000") return false;

  for (i=1; i<=9; i++) Soma = Soma + parseInt(strCPF.substring(i-1, i)) * (11 - i);
  Resto = (Soma * 10) % 11;

    if ((Resto == 10) || (Resto == 11))  Resto = 0;
    if (Resto != parseInt(strCPF.substring(9, 10)) ) return false;

  Soma = 0;
    for (i = 1; i <= 10; i++) Soma = Soma + parseInt(strCPF.substring(i-1, i)) * (12 - i);
    Resto = (Soma * 10) % 11;

    if ((Resto == 10) || (Resto == 11))  Resto = 0;
    if (Resto != parseInt(strCPF.substring(10, 11) ) ) return false;
    return true;
}

// Função para executar a validação do CPF antes de enviar o formulário
function validarCPF() {
    var cpfInput = document.getElementById('cpf');
    var strCPF = cpfInput.value.replace(/\D/g, ''); // Remove caracteres não numéricos

    if (!TestaCPF(strCPF)) {
        cpfInput.focus();
        cpfInput.classList.add('vibrar');
        setTimeout(function() {
            cpfInput.classList.remove('vibrar');
        }, 1000);
        return false;
    }
    return true;
}

document.getElementById('form-A').addEventListener('submit', function(event) {
    if (!validarCPF()) {
        event.preventDefault(); // Impede o envio do formulário se o CPF for inválido
    }
});