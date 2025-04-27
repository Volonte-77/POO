# creation des classe
# la classe boite a outils

class BoiteAOutis:
    #fonction magique
    def __init__(self,Outils=[]):
        self.Outils=Outils
        #fonctions liees aux outils
    def Ajouter_Outil(self,outil):
        self.Outils.append(outil)
    def Enlever_outil(self,outil):
        self.Outils.remove(outil)

#class marteau
class Marteau:
    # fonction magique
    def __init__(self,couleur="noire",poid="2k"):
        self.couleur=couleur
        self.poid=poid
    # fonction liees au marteau
    def Planter_clou(self):
        pass
    def Retirer_clou(self):
        pass
    def Peindre(self,couleur):
        self.couleur=couleur

#creation de la class tournevis

class Tournevis:
    #creation de la methode magique
    def __init__(self,taille,types="anneau"):
        self.taille=taille
        self.type=types
    #creation des methode lie au tournevis
    def Serrer_vis(self):
        print("le vis est serre")
    def Desserrer_vis(self):
        print("le vis est desserre")

#utilisation des mes class

boite1=BoiteAOutis(['vis','clou'])
boite1.Ajouter_Outil("bouro")
boite1.Enlever_outil('vis')
print(boite1.Outils)
    

    