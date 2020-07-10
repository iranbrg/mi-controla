let popUpInfo = document.getElementById('popUpInfo')
let popUpRetirada = document.getElementById('popUpRetirada')
let fundoPop = document.getElementById('fundoPop')

let testeMain = document.querySelector('main').children

// A variável "info_produto" é recebida por meio do atributo "data-info" e posteriormente deverá ser passada do JS para o HTML para que as informações do produto sejam exibidas nos pop-ups
// var info = document.getElementById("idDoBotao").getAttribute("data-info");

function exibirPopInfo() {
    popUpInfo.style.display = "grid";
    fundoPop.style.display = "block";
}

function retirarPopInfo() {
    popUpInfo.style.display = "none";
    fundoPop.style.display = "none";
}

function exibirPopRetirada() {
    popUpRetirada.style.display = "grid";
    fundoPop.style.display = "block";

}

function retirarPopRetirada() {
    popUpRetirada.style.display = "none";
    fundoPop.style.display = "none";

}