# verifier si le choix est valide ()
#   si la saisie n'est pas compee uniquement de hp du combattant est > 0 
#   renvoyer vrai
#  sinon
#   renvoyer faux

#verification si l'equipe est en vie  
#   pour chaque heros dans equipe:
#     si verifier si un combattant est en vie Vrai:
#       renvoyer Vrai
#   renvoyer Faux 

#obtenir le heros actif (equipe)
#   pour chaque heros dans equipe :
#     si verifier si un combattant est en vie est Vrai:
#         renvoyer heros
#   renvoyer RIEN  

#calculer les degats subis
#   degats = attaquant  - defenseur 
#   si degats <= 0 :
#      degats = 1
#   renvoyer degats 

#appliquer les degats
#   degats = calculer les degats subis 
#   defenseur["hp"] = defenseur["hp"] - degats
#   si defenseur["hp"] < 0 : 
#     defenseur["hp"] = 0
#   afficher "[attaquant.name] inflige [degats] degats a [defenseur.name]"



# 
#  generer un adversaire pour la vague (catalogue ennemis)
#     choisir un index aleatoire dans catalogue enemis 
#     tennemi modele = catalogue ennemis[index]
#     creer une copie neuve de cet ennemi avec ses PV max
#     renvoyer la copie neuve

# composer une equipe (heros_disponibles, taille_equipe)
#     equipe = liste vide
#     copie_catalogue = copie de heros_disponibles
#     
#     tant que taille de equipe < taille_equipe ET copie_catalogue n'est pas vide :
#         afficher "Choisissez le membre [taille de equipe + 1] de votre equipe :"
#         pour index, heros dans copie_catalogue :
#             afficher un combattant(heros, index + 1)
#             
#         demander saisie
#         si verifier si le choix est valide(saisie, 1, taille de copie_catalogue) :
#             index_choisi = entier(saisie) - 1
#             heros_selectionne = copie du heros a l'index_choisi
#             ajouter heros_selectionne dans equipe
#             retirer l'element a index_choisi de copie_catalogue
#             afficher "[heros_selectionne.name] rejoint l'equipe !"
#         sinon :
#             afficher message erreur
#             
#     renvoyer equipe

