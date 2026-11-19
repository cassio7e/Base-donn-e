from pymongo import MongoClient 


URL_MONGO = "mongodb://localhost:27017/"
NOM_BASE = "arene_rpg"

#display nombre option 
def afficher_nombre_disponibles(options, start=1):
#   parcourir une liste tout en gardant un numéro automatique pour chaque élément.
    for i, o in enumerate(options, start=start):
#      afficher (f"{index} = {o}) 
        print(f"{i} : {o}")


def obtenir_connexion():
    client = MongoClient("mongodb://localhost:27017/")
    db = client[NOM_BASE]
    return db

# charger les heros 
def charger_heros():
#   se brancher a la base 
    db = obtenir_connexion()
#   récuperer tous les documents dans la collection heros et les mettre dans une liste 
    heros =list(db.heros.find())
#   retourner la liste
    return heros 


# charger les ennemis 
def charger_ennemis():
#   se brancher a la base 
    db = obtenir_connexion()
#   récuperer tous les documents dans la collection heros 
#   les mettre dans une liste
    ennemis =list(db.ennemis.find())
#   retourner la liste 
    return ennemis


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
def enregistrer_partie(joueur, manches):
#   se brancher a la base 
    db = obtenir_connexion()
#   creer le doc avec le pseudo et le score
    document = {"joueur": joueur, "manches": manches}
#   inserer dans la collection Score
    db.palmares.insert_one(document)


# choix valide
def choix_valide(choix, min , max): 
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
        afficher_nombre_disponibles(options, start = 1)        
#       recuperer un choix avec un input
        choix = input("Choisi une option :")
#       si le choix est valide 
        if choix_valide(choix, 1, len(options)):
#           return choix en entier 
            return  int(choix)
#       afficher erreur
        print("Erreur")