document.addEventListener('DOMContentLoaded', function () {
    const dataNascimentoInput = document.getElementById('data_nascimento');
    dataNascimentoInput.addEventListener('input', validarData);

    function validarData() {
        const dataNascimento = dataNascimentoInput.value;
        const hoje = new Date();
        const dataSelecionada = new Date(dataNascimento);

        if (dataSelecionada > hoje) {
            dataNascimentoInput.setCustomValidity('A data de nascimento não pode ser no futuro.');
            dataNascimentoInput.classList.add('vibrar');
        } else {
            dataNascimentoInput.setCustomValidity('');
        }
    }
});