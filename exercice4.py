#creer une liste des 10 fruits, ajouter, et supprimer quelques un
fruits = ["banane", "orange", "kiwi", "cerise", "mangue", "ananas", "raisin", "peche", "abricot", "melon"]
fruits.append("papaye")
fruits.remove("kiwi")
print(fruits)
#modifier le duxieme element de la liste,afficher la longeur de la liste et trier la liste 
fruits[1] = "pomme"
print(len(fruits))
fruits.sort()
print(fruits)
