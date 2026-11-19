from utils import *
from game import lancer_partie, afficher_score_final
from db_init import preparer_base


def debut_jeux():
        preparer_base()
        while True:
                liste_choix =["Jouer", "Score", "Quitter"]
                choix = recuperer_choix_valide(liste_choix )
                if choix == 1:
                        lancer_partie()
                elif choix == 2:
                        afficher_scores()
                elif  choix == 3:
                        return 

debut_jeux()





