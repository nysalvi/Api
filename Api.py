from flask import Flask, redirect, request, make_response, render_template, url_for, send_from_directory
import requests
import Lanche
import json 

lanches = Lanche.lanches

def filtrar(_id, nome, preco, ctrlPreco, disponibilidade, estoque, ctrlEstoque):
    _lanches = lanches
    precisaFiltrar = True
    if _id != "0":
        _lanches = [x for x in lanches if x.id == _id]
        if len(_lanches) <= 1:
            precisaFiltrar = False
    if nome != "0" and precisaFiltrar:
        _lanches = [x for x in lanches if x.nome == nome]
        if len(_lanches) <= 1:
            precisaFiltrar = False    

    if ctrlPreco and preco != "0" and precisaFiltrar:                
        _lanches = [x for x in lanches if x.preco < preco] if ctrlPreco == "<" else [x for x in lanches if x.preco > preco]
        if len(_lanches) <= 1:
            precisaFiltrar = False
    elif preco != "0" and precisaFiltrar:
        _lanches = [x for x in lanches if x.preco == preco]
        if len(_lanches) <= 1:
            precisaFiltrar = False

    if disponibilidade and precisaFiltrar:
        _lanches = [x for x in lanches if x.disponibilidade == disponibilidade]
        if len(_lanches) <= 1:
            precisaFiltrar = False

    if ctrlEstoque and estoque != "0" and precisaFiltrar:
        _lanches = [x for x in lanches if x.estoque < estoque] if ctrlEstoque == "<" else [x for x in lanches if x.estoque > estoque]
        if len(_lanches) <= 1:
            precisaFiltrar = False    
    elif estoque != "0" and precisaFiltrar:
        _lanches = [x for x in lanches if x.estoque == estoque]
        if len(_lanches) <= 1:
            precisaFiltrar = False    
    return lanches if len(_lanches) == 0 else _lanches

app = Flask(__name__)

@app.route('/')
def index():
    icone = url_for('static', filename="./vegetarianfoodsvgrepocom.svg")
    panda = url_for('static', filename="./1555334508.svg")    
    
    return render_template("inicio.component.html", icone = icone, panda = panda)

@app.route("/cardapio")
def cardapio():    
    #argumento = request.args.get("argumento", default = "vazio", type = str)
    #return f'<p>Hello WORLD</p><p>{argumento}</p>'
    _id = request.args.get("id", default = "0", type = int)
    nome = request.args.get("nome", default = "0", type = str)
    preco = request.args.get("preco", default = "0", type = float)
    ctrlPreco = request.args.get("ctrlPreco", default = False, type = str)
    disponibilidade = request.args.get("disponivel", default = False, type = bool)
    estoque = request.args.get("estoque", default = "0", type = int)
    ctrlEstoque = request.args.get("ctrlEstoque", default = False, type = bool)

    lancheFiltrado = filtrar(_id, nome, preco, ctrlPreco, disponibilidade, estoque, ctrlEstoque)

    #return [x.toJson() for x in lancheFiltrado]    

    icone = url_for('static', filename="./vegetarianfoodsvgrepocom.svg")
    return render_template("cardapio.component.html", cardapio = lancheFiltrado, icone = icone)

@app.route("/api")
def api():    
    #argumento = request.args.get("argumento", default = "vazio", type = str)
    #return f'<p>Hello WORLD</p><p>{argumento}</p>'
    _id = request.args.get("id", default = "0", type = int)
    nome = request.args.get("nome", default = "0", type = str)
    preco = request.args.get("preco", default = "0", type = float)
    ctrlPreco = request.args.get("ctrlPreco", default = False, type = str)
    disponibilidade = request.args.get("disponivel", default = False, type = bool)
    estoque = request.args.get("estoque", default = "0", type = int)
    ctrlEstoque = request.args.get("ctrlEstoque", default = False, type = bool)

    lancheFiltrado = filtrar(_id, nome, preco, ctrlPreco, disponibilidade, estoque, ctrlEstoque)

    return [x.toJson() for x in lancheFiltrado]


@app.route("/buscar/")
def buscar():
    icone = url_for('static', filename="./vegetarianfoodsvgrepocom.svg")        
    return render_template("buscar.component.html", icone = icone)
