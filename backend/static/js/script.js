let popUpInfo = document.getElementById('popUpInfo')
let popUpRetirada = document.getElementById('popUpRetirada')
let fundoPop = document.getElementById('fundoPop')

function retirarPopInfo() {
    popUpInfo.style.display = "none";
    fundoPop.style.display = "none";
}

function retirarPopRetirada() {
    popUpRetirada.style.display = "none";
    fundoPop.style.display = "none";
}

function retirarPopRetiradaBotaoConfirma() {
    popUpRetirada.style.display = "none";
    fundoPop.style.display = "none";
}

var botoes = document.getElementsByClassName('detalheItem')

//não está reconhecendo o data-atribute como vetor. Quando reconhecer a função vai funcionar

for (i=0; i < botoes.length; i++){
   document.getElementById(botoes[i].id).addEventListener('click', dados);
}

function dados(){
    popUpInfo.style.display = "grid";
    fundoPop.style.display = "block";
    var vDados = this.getAttribute("data-info").split(",");
    document.getElementById('1').textContent = vDados[0];
    document.getElementById('2').textContent = vDados[1];
    document.getElementById('3').textContent = vDados[2];
    document.getElementById('4').textContent = vDados[3];
    document.getElementById('5').textContent = vDados[4];
    document.getElementById('6').textContent = vDados[5];
}

//Para o pop-up de retirada

var botoesRetirada = document.getElementsByClassName('bt')

for (i=0; i < botoesRetirada.length; i++){
    document.getElementById(botoesRetirada[i].id).addEventListener('click', dadosRetirada);
 }

function dadosRetirada(){
    popUpRetirada.style.display = "grid";
    fundoPop.style.display = "block";
    var vDadosR = this.getAttribute("data-info2").split(",");
    document.getElementById('1.1').textContent = vDadosR[0];
    document.getElementById('2.1').textContent = vDadosR[1];
    document.getElementById('3.1').textContent = vDadosR[2];
    document.getElementById('4.1').textContent = vDadosR[3];
    document.getElementById('5.1').textContent = vDadosR[4];
    preço = vDadosR[1];
}


let preço = 1;
let total;

function exibir (){
    var valorInput = document.getElementById('quantidadeR').value;
    Number(valorInput);
    total = preço*valorInput;
    let valorTotal = document.getElementById("valorTotal");
    valorTotal.textContent = total.toLocaleString('pt-br', {style: 'currency', currency: 'BRL'});
}


oninput = exibir;

//o id é o código de barras para os botões de retirar

let main = document.querySelector("main").children;

let numeroDeItens = 8;
let limitante = 4;
let altura = 178;

if (main.length <= 4 && main.length > 0) {
    fundoPop.style.height = "100%"
} else if (main.length <= 8 && main.length > 4) {
    fundoPop.style.height = "178%"
} 

while(true) {
    altura += 71;
    numeroDeItens += 4;
    limitante += 4;
    
    if (main.length > limitante && main.length <= numeroDeItens) {
    fundoPop.style.height = altura+"%";
    break
    }

}



