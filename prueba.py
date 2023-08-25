
#from flask import Flask,json # importamos flask
#app=Flask(__name__)     # creamos una aplicacion en flask
#@app.route("/anime")    # 
#def hello():            # 
#    return "Hello wordl"#

#if __name__=='__main__':
#    app.run()           #crear un metodo para q se ejecute flask

from flask import Flask, jsonify
app = Flask(__name__)

db=[
    {
        "id":1,
        "titulo":"Gintama: THE FINAL",
        "categoria":["action","comedy","drama","sci-fi"],
        "rating":"91%",
        "reviews":"33663 user",
        "season":"1 hour, 44 mins",
        "tipo":"movie",
        "img":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx114129-RLgSuh6YbeYx.jpg",
    },
    {
        "id":2,
        "titulo":"Gintama°",
        "categoria":["action","comedy","drama","sci-fi"],
        "rating":"90 %",
        "reviews":"87963 users",
        "season":"51 episodes",
        "tipo":"TV show",
        "img":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx20996-kBEGEGdeK1r7.jpg",
    },
    {
        "id":3,
        "titulo":"Fruits Basket: The Final",
        "categoria":["comedy","drama","psychological","romance","sci-fi"],
        "rating":"90%",
        "reviews":"118020 users",
        "season":"13 espisodes",
        "tipo":"TV Show",
        "img":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx124194-pWfBqp3GgjOx.jpg",
    },
    {
        "id":4,
        "titulo":"Hagane no Renkinjutsushi: FULLMETAL ALCHEMIST",
        "categoria":["action","adventure","drama","fantasy"],
        "rating":"90%",
        "reviews":"494524 users",
        "season":"64 episodes",
        "tipo":"TV Show",
        "img":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx5114-KJTQz9AIm6Wk.jpg",
    },
    {
        "id":5,
        "titulo":"Kaguya-sama wa Kokurasetai: Ultra Romantic",
        "categoria":["comedy","psychological","romance","sci-fi"],
        "rating":"90%",
        "reviews":"176923 users",
        "season":"13 episodes",
        "tipo":"TV Show",
        "img":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx125367-bl5vGalMH2cC.png",
    },
    {
        "id":6,
        "titulo":"Shingeki no Kyojin 3 Part 2",
        "categoria":["action","drama","fantasy","mystery"],
        "rating":"90%",
        "reviews":"411090 users",
        "season":"10 episodes",
        "tipo":"TV Show",
        "img":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx104578-LaZYFkmhinfB.jpg",
    },
    {
        "id":7,
        "titulo":"3-gatsu no Lion 2",
        "categoria":["drama","sci-fi"],
        "rating":"89%",
        "reviews":"102391 users",
        "season":"22 episodios",
        "tipo":"TV Show",
        "img":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx98478-dF3mpSKiZkQu.jpg",
    },
    {
        "id":8,
        "titulo":"HUNTERHUNTER (2011)",
        "categoria":["action","adventure","fantasy"],
        "rating":"89%",
        "reviews":"575350 users",
        "season":"148 episodes",
        "tipo":"TV Show",
        "img":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx11061-sIpBprNRfzCe.png",
    },
    {
        "id":9,
        "titulo":"Owarimonogatari (Ge)",
        "categoria":["comedy","mystery","psychological","romance","supernatural"],
        "rating":"89%",
        "reviews":"92090 users",
        "season":"7 episodes",
        "tipo":"TV Show",
        "img":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx21745-vHwC1VKoL6zf.png",
    },
    {
        "id":10,
        "titulo":"Steins;Gate",
        "categoria":["drama","psychological","sci-fi","thriller"],
        "rating":"89%",
        "reviews":"410650 users",
        "season":"24 episodes",
        "tipo":"TV Show",
        "img":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx9253-7pdcVzQSkKxT.jpg",
    }
]

@app.route("/")    
def hello():             
    return "Inicioooo"

@app.route('/anime', methods=["GET"])
def anime():
    return jsonify(db)

@app.route("/anime/<int:id>", methods=["GET"])
def animeId(id):
    anime_id = next((anime for anime in db if anime['id'] == int(id)), None)
    if anime_id:
        return jsonify(anime_id)
    else:
        return "Anime no encontrado", 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
