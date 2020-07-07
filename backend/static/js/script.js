let popUpInfo = document.getElementById('popUpInfo')
let popUpRetirada = document.getElementById('popUpRetirada')
let fundoPop = document.getElementById('fundoPop')

let testeMain = document.querySelector('main').children

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