from utils import *
from game import lancer_partie, afficher_score_final


# debut du jeux (principal)
def debut_jeux():
#     faire une liste de choix
        liste_choix =["Jouer", "Score", "Quitter"]
#       recupere les choix valide de la liste de choix 
        choix = recuperer_choix_valide(liste_choix )
#     SI le choix est 1 alors lancer le jeux
        if choix == 1:
               lancer_partie()
#     sinon 2 alors le afficher les scores
        elif choix == 2:
             afficher_score_final()
#     ou 3 quitter 
        elif  choix == 3:
             return 







