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
        vetorDeErros.push("1");
        window.scrollBy(0, -500)
    }

    if (inQuantidade.value == "") {
        mudarEstilo(inQuantidade);
        espacoMensagemErro[1].textContent = "Campo Obrigatório.";
        vetorDeErros.push("2");
        window.scrollBy(0, -400)
    } 
     
    if (inCodigoDeBarras.value == ""){
        mudarEstilo(inCodigoDeBarras);
        espacoMensagemErro[2].textContent = "Campo Obrigatório.";
        vetorDeErros.push("3");
        window.scrollBy(0, -300)
    }

    if (inPreco.value == ""){
        mudarEstilo(inPreco);
        espacoMensagemErro[3].textContent = "Campo Obrigatório.";
        vetorDeErros.push("4");
        window.scrollBy(0, -200);

    } 

    
    if (document.formAdd.tempo_entrega[0].checked == false 
    && document.formAdd.tempo_entrega[1].checked == false && 
    document.formAdd.tempo_entrega[2].checked == false ){
        espacoMensagemErro[4].textContent = "Selecione uma das opções.";
        vetorDeErros.push("5");
        window.scrollBy(0, -100)
    }

    if(inDescricao.value == " "){
        mudarEstilo(inDescricao);
        espacoMensagemErro[5].textContent = "Dê uma descrição para o produto.";
        vetorDeErros.push("6");
        window.scrollBy(0, -10)
    }

    
}

function limparEstilo (){
    voltarEstilo (inNome)
    voltarEstilo (inCodigoDeBarras)
    voltarEstilo (inQuantidade)
    voltarEstilo (inCodigoDeBarras)
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
    if (vetorDeErros.length == 0){
        document.getElementById("formAddProduto").submit();
    } else {
        vetorDeErros = [];
    }
}

function verificacaoInteiro () {
if (isNaN(inQuantidade.value)){
    
    mudarEstilo(inQuantidade);
    espacoMensagemErro[1].textContent = "Insira um valor numérico.";
    vetorDeErros.push("2");

} else if (!isNaN(inQuantidade.value)) {
    espacoMensagemErro[1].textContent = "";
    voltarEstilo (inQuantidade);
}

if (isNaN(inPreco.value)) {
        
    mudarEstilo(inPreco);
    espacoMensagemErro[3].textContent = "Insira um valor numérico.";
    vetorDeErros.push("4");
} else if (!isNaN(inQuantidade.value)) {
    espacoMensagemErro[3].textContent = "";
    voltarEstilo (inPreco);
}
}

verificacaoInteiro();
oninput = verificacaoInteiro;