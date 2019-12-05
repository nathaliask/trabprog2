import os
from peewee import *
import json
from playhouse.shortcuts import model_to_dict

arq = "loja.db"
db = SqliteDatabase(arq)

class BaseModel(Model):
    class meta():
        database = db

class Instrumento(BaseModel):
    nome = CharField()
    genero = ForeignKeyField(Genero)
    preco = FloatField()
    id_codigo = IntegerField()

class Vendedor(Model):
    nome = CharField()
    cpf = CharField()

class Pedido(Model):
    instrumento = ForeignKeyField(Instrumento)
    num_pedido = IntegerField()
    vendedor = ForeignKeyField(Vendedor)

class Genero(Model):
    nome = CharField()
    descricao = CharField()

class Fornecedor(Model):
    nome = CharField()
    cnpj = CharField()
    produtos = CharField()

class Cliente(Model):
    nome = CharField()
    cpf = CharField()
    telefone = CharField()

class Venda(Model):
    pedidos = ManyToManyField(Pedido)
    cliente = ForeignKeyField(Cliente)
    vendedor = ForeignKeyField(Vendedor)
    data = DateField()
    forma_compra = CharField()

class Site(Model):
    link = CharField()
    produtos_disp = ForeignKeyField(Catalogo)
    contatos = CharField()

class Local(Model):
    cep = CharField()
    rua = CharField()
    numero = IntegerField()
    bairro = CharField()
    cidade = CharField()

class Catalogo(Model):
    estoque = ManyToManyField(Insrumento)

if __name__ == "__main__":
    arq = "loja .db"
    if os.path.exists(arq):
        os.remove(arq)

try:
        db.connect()
        db.create_tables([Instrumento, Vendedor, Pedido, Genero, Fornecedor, Cliente, Venda, Venda.pedidos.get_through_model(), Site, Local, Catalogo, Catalogo.estoque.get_through_model()])

except OperationError as erro:
        print("erro ao criar as tabelas: "+str(erro))


luana = Vendedor.create(nome="luana", cpf="123.456.789.00")
vendedorlist= list(map(model_to_dict, Vendedor.select()))
samba = Genero.create(nome= "Samba", descricao= "Gênero musical e dança com origem na cidade brasileira do Rio de Janeiro.")
generolist= list(map(model_to_dict, Genero.select()))
multisom = Fornecedor.creator(nome= "Multisom", cnpj= "04.112.118.0001-62", produtos= "Cavaquinho")
fornecedorlist= list(map(model_to_dict, Fornecedor.select()))
endereço = Local.create(cep= "89037-385", rua= "Rua Sabiá", numero= "85", bairro= "Água Verde", cidade= "Blumenau")
locallist = list(map(model_to_dict, Local.select()))
cavaquinho = Instrumento.create(nome= "Cavaquinho", genero= samba, preco= 200.0, id_codigo= "222222")
instrumentolist = list(map(model_to_dict, Instrumento.select()))
pedido1 = Pedido.create(instrumento= cavaquinho, num_pedido= 1, vendedor= luana)
pedidolist = list(map(model_to_dict, Pedido.select()))
guilherme = Cliente.create(nome= "Guilherme", cpf= "046.378.439-01", telefone= "3333-3333")
clientelist = list(map(model_to_dict, Cliente.select()))
venda1 = Venda.create(pedidos= pedido1, cliente= guilherme, vendedor= luana, data= "2019-12-02", forma_compra= "Pelo site.")
catalogo1 = Catalogo.create(estoque= cavaquinho)
site1 = Site.create(link= "site.com", produtos_disp= catalogo1, contatos= "7777-7777")
sitelist = list(map(model_to_dict, Site.select()))
venda.pedidos.add(pedido1)
catalogo.estoque.add(cavaquinho)
vendalist = list(map(model_to_dict, Venda.select()))
catalogolist = list(map(model_to_dict, Catalogo.select()))

def lista():
    loja = [vendedorlist, generolist, fornecedorlist, locallist, instrumentolist, pedidolist, clientelist, sitelist, vendalist, catalogolist]
    return loja

