# main.py = afficher le menu et apeller les fichiers nécessaire

# debut du jeux (principal)
#     afficher le Menu,
#        afficher les 3 options numerotés 
#         Jouer, Score, Quitter
#     demander choix menu 
#        demander le choix du user 
#        recommencer tant une pas validé
#        renvoyé jusqua fontionnement 
#     Recuperer le choix valide 
#     si choix valide 
#       retourner le choix valide 
#     Si le choix est invalide
#       afficher le message erreur 
#     SI 1 alors lancer le jeux
#     sinon 2 alors le afficher les score 
#     ou 3 quitter 

#choix valide 
#si le choix n'est pas isdidgit()       
#   return false                        
#convertir le choix en entier 
#verifier que le choix est comprise entre les option min et max  
#dire si l'option dans le menu existe  

# afficher les scores
#     afficher message si vide
#     sinon afficher son score avec le rang 
#     montrer le meilleur resultat

# afficher choix invalide
#     afficher le message erreur 

# afficher quitter 
#     afficher mess de sorti 





####################################################################
#base de doneee






####################################################################
#interface UX


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






HERO = [
    {"name": "Leonardo", "attack": 14, "defense": 10, "hp": 120},
    {"name": "Raphael", "attack": 13, "defense": 13, "hp": 120},
    {"name": "Donatello", "attack": 20, "defense": 9, "hp": 120},
    {"name": "Michelangelo", "attack": 12, "defense": 20, "hp": 120},
]

ENNEMIE = [
    {"name": "Shredder", "attack": 11, "defense": 21, "hp": 120},
    {"name": "Krang", "attack": 13, "defense": 13, "hp": 120},
    {"name": "Bebop", "attack": 15, "defense": 10, "hp": 120},
    {"name": "Lord Dregg", "attack": 22, "defense": 20, "hp": 120},
]

##############################
# generer un adversaire pour la vague (catalogue ennemis)
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


