
#from flask import Flask,json # importamos flask
#app=Flask(__name__)     # creamos una aplicacion en flask
#@app.route("/anime")    # 
#def hello():            # 
#    return "Hello wordl"#

#if __name__=='__main__':
#    app.run()           #crear un metodo para q se ejecute flask

from flask import Flask,request, jsonify
app = Flask(__name__)

lista=[
    {
        "id":1,
        "titulo":"Gintama: THE FINAL",
        "poster":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx114129-RLgSuh6YbeYx.jpg",
        "categoria":["action","comedy","drama","sci-fi"],
        "rating":91,
        "reviews":33663,
        "season":"Winter 2021",
        "tipo":"movie",
        
    },
    {
        "id":2,
        "titulo":"Gintama°",
        "poster":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx20996-kBEGEGdeK1r7.jpg",
        "categoria":["action","comedy","drama","sci-fi"],
        "rating":90,
        "reviews":87963,
        "season":"Spring 2015",
        "tipo":"TV show",
    },
    {
        "id":3,
        "titulo":"Fruits Basket: The Final",
        "poster":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx124194-pWfBqp3GgjOx.jpg",
        "categoria":["comedy","drama","psychological","romance","sci-fi"],
        "rating":90,
        "reviews":118020,
        "season":"Spring 2021",
        "tipo":"TV Show",
    },
    {
        "id":4,
        "titulo":"Hagane no Renkinjutsushi: FULLMETAL ALCHEMIST",
        "poster":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx5114-KJTQz9AIm6Wk.jpg",
        "categoria":["action","adventure","drama","fantasy"],
        "rating":90,
        "reviews":494524,
        "season":"Spring 2009",
        "tipo":"TV Show",
    },
    {
        "id":5,
        "titulo":"Kaguya-sama wa Kokurasetai: Ultra Romantic",
        "poster":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx125367-bl5vGalMH2cC.png",
        "categoria":["comedy","psychological","romance","sci-fi"],
        "rating":90,
        "reviews":176923,
        "season":"Spring 2022",
        "tipo":"TV Show",
    },
    {
        "id":6,
        "titulo":"Shingeki no Kyojin 3 Part 2",
        "poster":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx104578-LaZYFkmhinfB.jpg",
        "categoria":["action","drama","fantasy","mystery"],
        "rating":90,
        "reviews":411090,
        "season":"Spring 2019",
        "tipo":"TV Show",
    },
    {
        "id":7,
        "titulo":"3-gatsu no Lion 2",
        "poster":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx98478-dF3mpSKiZkQu.jpg",
        "categoria":["drama","sci-fi"],
        "rating":89,
        "reviews":102391,
        "season":"Fall 2017",
        "tipo":"TV Show",
    },
    {
        "id":8,
        "titulo":"HUNTERHUNTER (2011)",
        "poster":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx11061-sIpBprNRfzCe.png",
        "categoria":["action","adventure","fantasy"],
        "rating":89,
        "reviews":575350,
        "season":"2011 - 2014",
        "tipo":"TV Show",
    },
    {
        "id":9,
        "titulo":"Owarimonogatari (Ge)",
        "poster":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx21745-vHwC1VKoL6zf.png",
        "categoria":["comedy","mystery","psychological","romance","supernatural"],
        "rating":89,
        "reviews":92090,
        "season":"Summer 2017",
        "tipo":"TV Show",
    },
    {
        "id":10,
        "titulo":"Steins;Gate",
        "poster":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx9253-7pdcVzQSkKxT.jpg",
        "categoria":["drama","psychological","sci-fi","thriller"],
        "rating":89,
        "reviews":410650,
        "season":"Spring 2011",
        "tipo":"TV Show",
    }
]

@app.route("/")    
def hello():             
    return "Pagina de Iniciooo"

@app.route("/anime", methods=["GET"])
def anime():
    return jsonify(lista)


@app.route("/anime", methods=["POST"])
def crear_anime():
    nuevo_anime = {
        "id": len(lista) + 1,  
        "titulo": request.json.get("titulo"),
        "poser": request.json.get("poster"),
        "categoria":request.json.get("categoria"),
        "rating":request.json.get("rating"),
        "reviews":request.json.get("reviews"),
        "season":request.json.get("season"),
        "tipo":request.json.get("tipo"),
    }
    lista.append(nuevo_anime)
    return jsonify(nuevo_anime), 201


@app.route("/anime/<int:id>", methods=["GET"])
def buscar_id(id):
    anime_id = next((anime for anime in lista if anime['id'] == int(id)), None)
    if anime_id:
        return jsonify(anime_id)
    else:
        return "No se encontro el anime", 404


@app.route("/anime/<int:id>", methods=["DELETE"])
def delete(id):
    anime_id = next((anime for anime in lista if anime['id'] == int(id)), None)
    if anime_id:
        lista.remove(anime_id)
        return jsonify({"message": "Anime eliminado"}), 200
    else:
        return "No se encontro el anime", 404


@app.route("/anime/<int:id>", methods=["PUT"])
def put_total(id):
    anime_id = next((anime for anime in lista if anime['id'] == int(id)), None)
    if anime_id:
        anime_id.update(request.json)
        return jsonify(anime_id), 200
    else:
        return "No se encontro el anime", 404


@app.route("/anime/<int:id>", methods=["PATCH"])
def patch_parcial(id):
    anime_id = next((anime for anime in lista if anime['id'] == int(id)), None)
    if anime_id:
        data = request.json
        for key, value in data.items():
            if key in anime_id:
                anime_id[key] = value
        return jsonify(anime_id), 200
    else:
        return "No se encontro el anime", 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
