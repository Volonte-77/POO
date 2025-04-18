#declaration des variables,nom,age,taille,et etudiant=en bouleen
nom = "Dupont"
prenom = "Jean"
age = 25
taille = 1.75
etudiant = True
#affichage des variables avec f-string
print(f"Bonjour, je suis {prenom} {nom}, j'ai {age} ans, je mesure {taille} m et je suis étudiant : {etudiant}")
#utiliser la fonction type pour afficher le type de chaque variable
print(f"Le type de la variable nom est : {type(nom)}")
print(f"Le type de la variable prenom est : {type(prenom)}")
print(f"Le type de la variable age est : {type(age)}")
print(f"Le type de la variable taille est : {type(taille)}")
print(f"Le type de la variable etudiant est : {type(etudiant)}")
#utiliser la fonction dir pour afficher les attributs et methodes de chaque variable