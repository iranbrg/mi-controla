from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, SelectField, SubmitField, RadioField, TextAreaField
from wtforms.validators import DataRequired, Optional


class NovoProduto(FlaskForm):
    nome_produto = StringField("Nome do Produto", validators=[
                               DataRequired(message="Campo obrigatório")])

    quantidade = IntegerField("Quantidade", validators=[
                              DataRequired(message="Campo obrigatório")])

    codigo_de_barras = StringField("Código de Barras", validators=[
                                   DataRequired(message="Campo obrigatório")])

    preco = DecimalField("Preço", validators=[
                         DataRequired(message="Campo obrigatório")])

    fornecedor = SelectField("Selecione o fornecedor do produto", choices=[("americanas", "Americanas"), (
        "amazon", "Amazon"), ("mercadolivre", "Mercado Livre")], validators=[DataRequired(message="Campo obrigatório")])

    tempo_entrega = RadioField("Tempo de Entrega", choices=[("7", "7 Dias"), ("14", "14 Dias"), (
        "30", "30 Dias")], validators=[DataRequired(message="Campo obrigatório")])

    descricao = StringField("Descrição")

    inserir_produto = SubmitField("Inserir Produto")
