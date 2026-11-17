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


##########################################################################
#reinitialiser la collection (remise a l'origine)
 #   reinitialiser la collection existante
  #  inserrer une copie des doc de depart donc des ennemies et des heros

#reinitialiser la base pour mettre les combattants de depart 
 #   remettre les heros 
  #  remettre les ennemis 

####################################################################

#charger pour renvoyer la liste des heros dispo 
#    lire la collection heros 
#   les mettre dans une liste 
#
#charger pour renvoyer la liste des ennemis dispo 
#    lire la collection ennemis 
#    les mettre dans une liste 

#enregistrer la sauvegarde 
#    supprimer l'ancienne sauvegarde du joueur 

#charger le palmares 
#    lire tous les scores
#    les trier du plus grand au plus petit nomre de manche 

#enregistrer la partie 
#    creer le document du score 
#    inserer dans la collection palmares 







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
