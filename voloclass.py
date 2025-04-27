# les bases de class

class Rectangle:
    def __init__(self,longeur,largeur,couleur="red"):
         self.longuer=longeur
         self.largeur=largeur
         self.couleur=couleur
    #calculer surface
    def calculer_surface(self):
         return self.longuer*self.largeur

rectanglejamal=Rectangle(12,6)
print(rectanglejamal.longuer)
rectanglejamal.couleur="yellow"
surface=rectanglejamal.calculer_surface()
print(surface)

   
    
