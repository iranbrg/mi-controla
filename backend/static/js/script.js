let popUpInfo = document.getElementById('popUpInfo')
let popUpRetirada = document.getElementById('popUpRetirada')
let fundoPop = document.getElementById('fundoPop')



// A variável "info_produto" é recebida por meio do atributo "data-info" e posteriormente deverá ser passada do JS para o HTML para que as informações do produto sejam exibidas nos pop-ups
// var info = document.getElementById("idDoBotao").getAttribute("data-info");


function retirarPopInfo() {
    popUpInfo.style.display = "none";
    fundoPop.style.display = "none";
}


function retirarPopRetirada() {
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
    var vDados = this.getAttribute("data-info");
    document.getElementById('1').textContent = vDados[0];
    document.getElementById('2').textContent = vDados[1];
    document.getElementById('3').textContent = vDados[2];
    document.getElementById('4').textContent = vDados[3];
    document.getElementById('5').textContent = vDados[4];
    document.getElementById('6').textContent = vDados[5];
}

console.log(botoes);

//Para o pop-up de retirada

var botoesRetirada = document.getElementsByClassName('bt')

for (i=0; i < botoesRetirada.length; i++){
    document.getElementById(botoesRetirada[i].id).addEventListener('click', dadosRetirada);
 }

function dadosRetirada(){
    popUpRetirada.style.display = "grid";
    fundoPop.style.display = "block";
    var vDadosR = this.getAttribute("data-info2");
    document.getElementById('1.1').textContent = vDadosR[0];
    document.getElementById('2.1').textContent = vDadosR[1];
    document.getElementById('3.1').textContent = vDadosR[2];
    document.getElementById('4.1').textContent = vDadosR[3];
    document.getElementById('5.1').textContent = vDadosR[4];
    console.log(vDadosR);
}

//o id é o código de barras para os botões de retirar
