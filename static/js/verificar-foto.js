"use strict" // Habilita o modo estrito do JS para evitar erros

let photo = document.getElementById("imgAvatar") // Obtém a referência do elemento de imagem do avatar
let file = document.getElementById("flImage") // Obtém a referência do elemento de entrada do arquivo

photo.addEventListener("click", () => {
    file.click(); // Ao clicar na imagem do avatar, aciona o clique do elemento de entrada do arquivo
});

file.addEventListener("change", () => {

    if (file.files.length <= 0) {
        return; // Se nenhum arquivo for selecionado, retorna sem fazer nada
    }

    let reader = new FileReader(); // Cria uma instância do objeto FileReader

    reader.onload = () => {
        photo.src = reader.result; // Define a imagem do avatar com o resultado da leitura do arquivo
    }

    reader.readAsDataURL(file.files[0]); // Lê o conteúdo do arquivo como uma URL de dados e aciona o evento onload quando concluído

});
