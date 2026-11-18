from utils import choix_valide

# debut du jeux (principal)
def debut_jeux():
#     demander choix valide
        while True:
#         tant que infini
            while True:

#               parcourir une liste tout en gardant un numéro automatique pour chaque élément.
                for index, option in enumerate(option, start=1):
                    print(f"{index}. {option}")
#               demander le choix du user
                choix = input("Votre choix :")
#               Si choix valide 
                if choix_valide(choix):
#               retourne le choix valide en entier
                    return choix_valide
                    break 
#              afficher message erreur
                print("Choix invalide, réessaye")
#     SI 1 alors lancer le jeux
        if choix_valide(choix) == 1:
            lancer_partie()
#     sinon 2 alors le afficher les score
        elif choix_valide(choix) == 2:
             lancer_score(score)
#     ou 3 quitter 
        elif  choix_valide(choix) == 3:
             return 







