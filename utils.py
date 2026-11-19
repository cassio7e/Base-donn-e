from game import afficher_nombre_disponible
from pymongo import MongoClient 

URL_MONGO = "mongodb://localhost:27017/"
NOM_BASE = "arene_rpg"


# charger les heros 
def charger_heros():
#   se brancher a la base 
    db = obtenir_connexion()
#   récuperer tous les documents dans la collection heros et les mettre dans une liste 
    heros =list(db.heros.find())
#   retourner la liste
    return heros 
# 
# charger les ennemis 
def charger_ennemis():
#   se brancher a la base 
    db = obtenir_connexion()
#   récuperer tous les documents dans la collection heros 
#   les mettre dans une liste
    ennemis =list(db.ennemis.find())
#   retourner la liste 
    return ennemis
# 
# charger le palmares (renvoyer le classement des meilleurs scores)
def charger_score():
#   se brancher a la base 
    db = obtenir_connexion()
#   recuperer tous les documents de la collection Scores
 #   trier par nombre de manche decroissante
#       les mettre en liste
    score = list(db.score.find().sort("manches", -1))
#        retourner la liste
    return score

# enregistrer la partie (sauvegarde des resultats)
def enregistrer_partie():
#   se brancher a la base 
    db = obtenir_connexion()
#   creer le doc avec le pseudo et le score
    document = {"joueur": joueur, "manches": manches}
#   inserer dans la collection Score
    db.palmares.insert_one(document)

# choix valide
def choix_valide(choix): 
#   si le choix n'est pas composé uniquement de chiffre          
    if not choix.isdigit():
#       return false        
        return False                      
#   convertir le choix en entier
    nombre = int(choix)
#  return True si le choix est entre min et max inclus
    return min <= nombre <= max

#recuperer choix valide 
def recuperer_choix_valide(options):
#   tant que vrai 
    while True:
#       afficher les options
        afficher_nombre_disponible(options)        
#       recuperer un choix avec un input
        choix = input("Choisi un nombre :")
#       si le choix est valide 
        if choix_valide():
#           return choix en entier 
            return  int(choix)
#       afficher erreur
        print("Erreur")