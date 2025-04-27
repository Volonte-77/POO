#creation de la classe film

class Film:
    def __init__(self,titre,genre,duree,annee):
        self.titre=titre
        self.genre=genre
        self.duree=duree
        self.annee=annee
    # creation de la methode watch
    def watch(self):
        print("Regarder le film",self.titre)   
    def afficher(self):
        print("Titre:",self.titre)
        print("Genre:",self.genre)
        print("Durée:",self.duree,"minutes")
        print("Année de sortie:",self.annee)
        print("-----------------------------")
# creation de la class FilmCassette
class FilmCassette(Film):
    pass 
#creation des objets

film=Film("Inception","Science-fiction",148,2010)
film.afficher()
film.watch()
film_cassette=FilmCassette("Titanic","Romance",195,1997)
film_cassette.afficher()
film_cassette.watch()
#
