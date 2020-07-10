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

let preço = 2;
let total;

function exibir (){
    var valorInput = document.getElementById('quantidadeR').value;
    Number(valorInput);
    total = preço*valorInput;
    let valorTotal = document.getElementById("valorTotal");
    valorTotal.textContent = total.toLocaleString('pt-br', {style: 'currency', currency: 'BRL'});
}


oninput = exibir; 


