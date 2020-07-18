let popUpConfirmacao = document.getElementById("popUpConfirmacao");
let fundoPop = document.getElementById("fundoPop");
let botãoInserir = document.querySelector(".boton");

function alerta() {
  window.alert("Produto adicionado com sucesso!")
}


var espacoMensagemErro = document.getElementsByClassName("erro");
var vetorDeErros = [];

function mudarEstilo (input) {
     input.style.borderColor = "#c50000d0";
     input.style.borderStyle = "solid";
}

function voltarEstilo (input){
    input.style.borderColor = "transparent";
    input.style.borderStyle = "none";
}

   var inNome = document.getElementById("nome_produto");
   var inQuantidade = document.getElementById("quantidade");
   var inCodigoDeBarras = document.getElementById("codigo_barras");
   var inPreco = document.getElementById("preco");
   var inDescricao = document.getElementById("descricao");


function verificação (){

    if (inNome.value == ""){
        mudarEstilo(inNome);
        espacoMensagemErro[0].textContent = "Preencha o nome do produto.";
        window.scrollBy(0, -500)
    }

    if (inQuantidade.value == "") {
        mudarEstilo(inQuantidade);
        espacoMensagemErro[1].textContent = "Campo Obrigatório.";
        window.scrollBy(0, -400)
    } 
     
    if (inCodigoDeBarras.value == ""){
        mudarEstilo(inCodigoDeBarras);
        espacoMensagemErro[2].textContent = "Campo Obrigatório.";
        window.scrollBy(0, -300)
    }

    if (inPreco.value == ""){
        mudarEstilo(inPreco);
        espacoMensagemErro[3].textContent = "Campo Obrigatório.";
        window.scrollBy(0, -200);

    } 

    
    if (document.formAdd.tempo_entrega[0].checked == false 
    && document.formAdd.tempo_entrega[1].checked == false && 
    document.formAdd.tempo_entrega[2].checked == false ){
        espacoMensagemErro[4].textContent = "Selecione uma das opções.";
        window.scrollBy(0, -100)
    }

    if(inDescricao.value == " "){
        mudarEstilo(inDescricao);
        espacoMensagemErro[5].textContent = "Dê uma descrição para o produto.";
        window.scrollBy(0, -10)
    }

    
}

function limparEstilo (){
    voltarEstilo (inNome)
    voltarEstilo (inCodigoDeBarras)
    voltarEstilo (inQuantidade)
    voltarEstilo (inPreco)
    voltarEstilo (inDescricao)
    espacoMensagemErro[0].textContent = "";
    espacoMensagemErro[1].textContent = "";
    espacoMensagemErro[2].textContent = "";
    espacoMensagemErro[3].textContent = "";
    espacoMensagemErro[4].textContent = "";
    espacoMensagemErro[5].textContent = "";
}

function açãoBotão (){
    limparEstilo();
    verificação();
}

function executarOnInput () {

//verificaao inteiro
if (isNaN(inQuantidade.value)){
    
    mudarEstilo(inQuantidade);
    espacoMensagemErro[1].textContent = "Insira um valor numérico.";

} else if (!isNaN(inQuantidade.value) && inQuantidade.value != "") {
    espacoMensagemErro[1].textContent = "";
    voltarEstilo (inQuantidade);
}

if (isNaN(inPreco.value)) {
        
    mudarEstilo(inPreco);
    espacoMensagemErro[3].textContent = "Insira um valor numérico.";
} else if (!isNaN(inPreco.value) && inPreco.value != "") {
    espacoMensagemErro[3].textContent = "";
    voltarEstilo (inPreco);
}

//limparEstiloOnInptut
if(inNome.value !== ""){
    voltarEstilo(inNome)
    espacoMensagemErro[0].textContent = "";
}
if(inCodigoDeBarras.value !== ""){
    voltarEstilo(inCodigoDeBarras);
    espacoMensagemErro[2].textContent = "";
}
if(document.formAdd.tempo_entrega[0].checked == true 
 || document.formAdd.tempo_entrega[1].checked == true || 
 document.formAdd.tempo_entrega[2].checked == true ){
     espacoMensagemErro[4].textContent = "";
 }
if(inDescricao.value !== " "){
    voltarEstilo(inDescricao)
    espacoMensagemErro[5].textContent = "";
}
}

function verificacaoInteiro () {
    if (isNaN(inQuantidade.value)){
        
        mudarEstilo(inQuantidade);
        espacoMensagemErro[1].textContent = "Insira um valor numérico.";
    
    } else if (!isNaN(inQuantidade.value) && inQuantidade.value != "") {
        espacoMensagemErro[1].textContent = "";
        voltarEstilo (inQuantidade);
    }
    
    if (isNaN(inPreco.value)) {
            
        mudarEstilo(inPreco);
        espacoMensagemErro[3].textContent = "Insira um valor numérico.";
    } else if (!isNaN(inPreco.value) && inPreco.value != "") {
        espacoMensagemErro[3].textContent = "";
        voltarEstilo (inPreco);
    }
    }

verificacaoInteiro();
oninput = executarOnInput;
