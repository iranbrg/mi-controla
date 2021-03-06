from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_uploads import UploadSet, IMAGES, configure_uploads
from wtforms import StringField, IntegerField, DecimalField, SelectField, SubmitField, RadioField, HiddenField
from wtforms.validators import DataRequired, NumberRange
from backend import app

images = UploadSet('images', IMAGES)
configure_uploads(app, images)

class NovoProduto(FlaskForm):
    nome_produto = StringField("Nome do Produto", validators=[DataRequired(message="Campo obrigatório")])

    quantidade = IntegerField("Quantidade", validators=[DataRequired(message="Campo obrigatório")])

    codigo_barras = StringField("Código de Barras", validators=[DataRequired(message="Campo obrigatório")])

    preco = DecimalField("Preço", validators=[DataRequired(message="Campo obrigatório")])

    fornecedor = SelectField("Selecione o fornecedor do produto", choices=[("Americanas", "Americanas"), ("Amazon", "Amazon"), ("Mercado Livre", "Mercado Livre")], validators=[DataRequired(message="Campo obrigatório")])

    tempo_entrega = RadioField("Tempo de Entrega", choices=[("7 dias", "7 dias"), ("14 dias", "14 dias"), ("30 dias", "30 dias")], validators=[DataRequired(message="Campo obrigatório")])

    descricao = StringField("Descrição", default=" ")

    imagem_produto = FileField("Imagem do produto", validators=[FileAllowed(images, message=f"Formatos de imagens permitidos: {IMAGES}")])

    inserir_produto = SubmitField("Inserir Produto")
    
class RetirarProduto(FlaskForm):
    quantidadeR = IntegerField(validators=[DataRequired(message="Quantidade obrigatória"), NumberRange(min=1)])

    hidden_nome_produto = HiddenField()
    
    botaoCR = SubmitField("Retirar Produto")

class RemoverProduto(FlaskForm):
    hidden_nome_produto = HiddenField()
    
    botaoexcluir = SubmitField("REMOVER")