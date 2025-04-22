# les fonction sans parametre
def afficher_message():
    print("Bonjour, comment ca va ?")
afficher_message()

#les fonctions avec parametre
def afficher_nom_prenom(nom,prenom):
    print(f"Nom: {nom}")
    print(f"Prenom: {prenom}")
afficher_nom_prenom("Malisava","Volonte")

#utiliser une fonction avec une valeur de retour
def calculer_somme(a,b):
    resultat=a+b
    return resultat
Age=calculer_somme(10,7)
print(f"{Age} ans")

