import requests
import json

class Lanche(object):
    def __init__(self, _id, nome, preco, disponibilidade, estoque, imagem):        
        self.id = _id
        self.nome = nome
        self.preco = preco 
        self.disponibilidade = disponibilidade
        self.estoque = estoque        
        self.imagem = imagem
    def __repr__(self):
        disponibilidade = ("Indisponivel", "Disponivel")[self.disponibilidade]
        return "{}({}) : {}".format(self.nome, disponibilidade, self.preco)     
    def toJson(self):
        this = {
            "id" : self.id,
            "nome" : self.nome,
            "preco" : self.preco, 
            "disponibilidade" : self.disponibilidade,
            "estoque" : self.estoque,
            "imagem" : self.imagem
            }
        return this
###########################################################################################

imagens = {}
lanches = []

def carregaImagens():
    """    
    burguerJson = requests.get("https://api.spoonacular.com/food/menuItems/search?query=burger&number=8&apiKey=87a35345b372471ba05e7ba7c5286918").json()    
    donut_pastelJson = requests.get("https://api.spoonacular.com/food/menuItems/search?query=pastry&number=12&apiKey=87a35345b372471ba05e7ba7c5286918").json()

    sanduicheJson = requests.get("https://api.spoonacular.com/food/menuItems/search?query=sandwich&number=3&apiKey=87a35345b372471ba05e7ba7c5286918").json()
    redbullJson= requests.get("https://api.spoonacular.com/food/menuItems/search?query=energy%20drink&number=1&apiKey=87a35345b372471ba05e7ba7c5286918").json()
    sucoJson = requests.get("https://api.spoonacular.com/food/menuItems/search?query=orange-juice&number=3&apiKey=87a35345b372471ba05e7ba7c5286918").json()
    aguaJson = requests.get("https://api.spoonacular.com/food/menuItems/search?query=Water&number=5&apiKey=87a35345b372471ba05e7ba7c5286918").json()
    sodaJson = requests.get("https://api.spoonacular.com/food/menuItems/search?query=soda&number=2&apiKey=87a35345b372471ba05e7ba7c5286918").json()

    boloJson = requests.get("https://api.spoonacular.com/food/menuItems/search?query=cake&number=3&apiKey=87a35345b372471ba05e7ba7c5286918").json()
    croissantJson = requests.get("https://api.spoonacular.com/food/menuItems/search?query=croissant&number=1&apiKey=87a35345b372471ba05e7ba7c5286918").json()
    tortaJson = requests.get("https://api.spoonacular.com/food/menuItems/search?query=pie&number=2&apiKey=87a35345b372471ba05e7ba7c5286918").json()
    sorveteJson = requests.get("https://api.spoonacular.com/food/menuItems/search?query=ice%20cream&number=3&apiKey=87a35345b372471ba05e7ba7c5286918").json()
    almocoJson = requests.get("https://api.spoonacular.com/food/menuItems/search?query=dinner&number=7&apiKey=87a35345b372471ba05e7ba7c5286918").json()    
    """

    """    
    donut_pastelJson = burguerJson 
    
    sanduicheJson = burguerJson 
    redbullJson= burguerJson 
    sucoJson = burguerJson 
    aguaJson = burguerJson 
    sodaJson = burguerJson 

    boloJson = burguerJson 
    croissantJson = burguerJson 
    tortaJson = burguerJson 
    picoleJson = burguerJson 
    almocoJson = burguerJson 
    """

    """
    burguerImagem = burguerJson["menuItems"][7]["image"]       
    donutImagem = donut_pastelJson["menuItems"][11]["image"]        
    pastelImagem = donut_pastelJson["menuItems"][3]["image"]        
    sanduicheImagem = sanduicheJson["menuItems"][2]["image"]
    redbullImagem = redbullJson["menuItems"][0]["image"]
    sucoImagem = sucoJson["menuItems"][2]["image"]  
    aguaImagem = aguaJson["menuItems"][4]["image"]
    sodaImagem = sodaJson["menuItems"][1]["image"]
    boloCenouraImagem = boloJson["menuItems"][0]["image"]
    boloChocolateImagem = boloJson["menuItems"][2]["image"]
    tortaImagem = tortaJson["menuItems"][1]["image"]
    croissantImagem = croissantJson["menuItems"][0]["image"]
    sorveteImagem = sorveteJson["menuItems"][2]["image"]
    almocoImagem = almocoJson["menuItems"][6]["image"]
    """

    """
    burguerImagem = burguerJson
    donutImagem = donut_pastelJson
    pastelImagem = donut_pastelJson
    sanduicheImagem = sanduicheJson
    redbullImagem = redbullJson
    sucoImagem = sucoJson
    aguaImagem = aguaJson
    sodaImagem = sodaJson
    boloCenouraImagem = boloJson
    boloChocolateImagem = boloJson
    tortaImagem = tortaJson
    croissantImagem = croissantJson
    picoleImagem = picoleJson
    almocoImagem = almocoJson
    """

    """
    imagens['burguer'] = burguerImagem
    imagens['donut'] = donutImagem
    imagens['pastel'] = pastelImagem
    imagens['sanduiche'] = sanduicheImagem
    imagens['redbull'] = redbullImagem
    imagens['suco'] = sucoImagem
    imagens['agua'] = aguaImagem
    imagens['soda'] = sodaImagem
    imagens['boloCenoura'] = boloCenouraImagem
    imagens['boloChocolate'] = boloChocolateImagem
    imagens['torta'] = tortaImagem
    imagens['croissant'] = croissantImagem
    imagens['sorvete'] = sorveteImagem
    imagens['almoco'] = almocoImagem
    """
    Imagem = open("imagem.png", "r")
    #Imagem = "https://MeDaAsIbagems.com.br"
    imagens['burguer'] = Imagem
    imagens['donut'] = Imagem
    imagens['pastel'] = Imagem
    imagens['sanduiche'] = Imagem
    imagens['redbull'] = Imagem
    imagens['suco'] = Imagem
    imagens['agua'] = Imagem
    imagens['soda'] = Imagem
    imagens['boloCenoura'] = Imagem
    imagens['boloChocolate'] = Imagem
    imagens['torta'] = Imagem
    imagens['croissant'] = Imagem
    imagens['sorvete'] = Imagem
    imagens['almoco'] = Imagem


def popular():
    burguer = Lanche(1, "Burguer", 8, True, 10, imagens["burguer"])
    donut = Lanche(2, "Donut", 3, True, 20, imagens["donut"])        
    pastel = Lanche(3, "Pastel", 6, True, 8, imagens["pastel"])
    sanduiche = Lanche(4, "Sanduiche", 6, True, 20, imagens["sanduiche"])
    redbull = Lanche(5, "Redbull", 5, True, 12, imagens["redbull"])
    suco = Lanche(6, "Suco", 5.50, True, 10, imagens["suco"])
    agua = Lanche(7, "Agua", 3.50, True, 20, imagens["agua"])
    soda = Lanche(8, "Soda", 4.50, True, 15, imagens["soda"])
    boloDeChocolate = Lanche(9, "Bolo de Chocolate", 12, True, 4, imagens["boloChocolate"])
    boloDeCenoura = Lanche(10, "Bolo de Cenoura", 6, True, 4, imagens["boloCenoura"])
    croissantDeChocolate = Lanche(11, "Croissant de chocolate", 5, True, 30, imagens["croissant"])
    tortaDeChocolate = Lanche(12, "Torta de chocolate", 5, True, 7, imagens["torta"])
    sorvete = Lanche(13, "Sorvete", 2.50, True, 19, imagens["sorvete"])
    almoco = Lanche(14, "Almoco", 18.50, True, 19, imagens["almoco"])

    lanches.append(burguer)
    lanches.append(donut)
    lanches.append(pastel)
    lanches.append(sanduiche)
    lanches.append(redbull)
    lanches.append(suco)
    lanches.append(agua)
    lanches.append(soda)
    lanches.append(boloDeChocolate)
    lanches.append(boloDeCenoura)
    lanches.append(croissantDeChocolate)
    lanches.append(tortaDeChocolate)
    lanches.append(sorvete)
    lanches.append(almoco)
        
carregaImagens()
popular()

#burguer
#coffee
#almoco
#Pastel Assado de Carne
#Pastel Frito de Carne

""" 
    dadosJson = requests.get("https://api.spoonacular.com/food/menuItems/search?query=burger&number=15&apiKey=87a35345b372471ba05e7ba7c5286918").json()
    imagem = dadosJson["menuItems"][7]["image"]
    burguer = Lanche(1, "Pastel", 14, False, 20, imagem)
    lanches.append(burguer)


    dadosJson = requests.get("https://api.spoonacular.com/food/menuItems/search?query=burger&number=2&apiKey=87a35345b372471ba05e7ba7c5286918").json()
    imagem = dadosJson["menuItems"][0]["image"]
    print(imagem)
    imagemArquivo = requests.get(imagem).content
    print("5")
    #print(imagemArquivo)
"""
