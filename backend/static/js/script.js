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
    document.getElementById('quantidadeR').value = "";
    popUpRetirada.style.display = "grid";
    fundoPop.style.display = "block";
    var vDadosR = this.getAttribute("data-info2").split(",");
    document.getElementById('1.1').textContent = vDadosR[0];
    document.getElementById('2.1').textContent = vDadosR[1];
    document.getElementById('3.1').textContent = vDadosR[2];
    document.getElementById('4.1').textContent = vDadosR[3];
    document.getElementById('5.1').textContent = vDadosR[4];
    preço = vDadosR[1];
    document.getElementById("passarNome").value = vDadosR[0];
    quantidadeDoProdutoPop = vDadosR[6];
}

let quantidadeDoProdutoPop = 0;

let preço = 1;
let total;

function exibir (){
    var valorInput = document.getElementById('quantidadeR').value;
    Number(valorInput);
    total = preço*valorInput;
    let valorTotal = document.getElementById("valorTotal");
    valorTotal.textContent = total.toLocaleString('pt-br', {style: 'currency', currency: 'BRL'}); 
    if (valorInput > quantidadeDoProdutoPop){
        document.getElementById("mensagemErroEx").textContent = "A quantidade que você selecionou é maior do que o disponível em estoque"
        document.getElementById('quantidadeR').value = "";
        document.getElementById("valorTotal").textContent = "R$ 0,00"
    } else{
        document.getElementById("mensagemErroEx").textContent = "";
    }
   
}


oninput = exibir;

//o id é o código de barras para os botões de retirar