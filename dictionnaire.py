#creons un dictionnaire des nouvelle_campagnes,nom du campagne,date de debut responsabledeu campage, influenceurs_importants
nouvelle_campagnes = {
    "responsable_campagne": "Dupont",
    "date_debut": "2023-10-01",
    "nom_campagne": "Campagne de Noël",
    "influenceurs_importants": ["Influenceur1", "Influenceur2", "Influenceur3"],
    "budget": 10000,
    "plateforme": "Instagram",
}
#afficher le dictionnaire
print(nouvelle_campagnes)
#afficher le nom de la campagne 
print(nouvelle_campagnes["nom_campagne"])
#changer le nom de la campagne
nouvelle_campagnes["nom_campagne"] = "Campagne de Printemps"
#afficher le nom de la campagne
print(nouvelle_campagnes["nom_campagne"])
#changer la valeur du budget
nouvelle_campagnes["budget"] = 15000
#suppimer un influenceur de la liste
nouvelle_campagnes["influenceurs_importants"].remove("Influenceur2")
#afficher le dictionnaire
print(nouvelle_campagnes)
#supprimer un dictionnaire
del nouvelle_campagnes["responsable_campagne"]