from pymongo import MongoClient 


URL_MONGO = "mongodb://localhost:27017/"
NOM_BASE = "arene_rpg"

#display nombre options 
def afficher_nombre_disponibles(options, start=1):
#   parcourir une liste tout en gardant un numéro automatique pour chaque élément.
    for i, o in enumerate(options, start=start):
#      afficher (f"{index} = {o}) 
        print(f"{i} : {o}")

#   fonction pour se brancher a la base 
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
#   récuperer tous les documents dans la collection heros et les mettre dans une liste
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
    score = list(db.scores.find({}, {"_id": 0}))
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


#afficher les 3 premiers scores
def afficher_scores():
#   charger les scores depuis la base 
    scores = charger_score()
#   si aucun il n'y a pas de score 
    if not scores:
#       afficher un message comme quoi il n'y a rien d'enregistrer
        print("Aucun score enregistré actuellement")
#       return 
        return
#   afficher un titre    
    print("----------SCORES----------")
#   trier les scores par nombre de manches decroissante
    scores_tries = sorted(scores, key=lambda x:x['manches'], reverse=True)
#   afficher les 3 meilleurs scores 
    for rang, doc in enumerate(scores_tries[:3], start=1):
        print(f"{rang}. {doc['joueur']} - {doc['manches']} manches")
#        un message pour dire que le joueur appuie sur Entrée pour revenir au menu
        input("Si tu veux revenir au menu appuis sur Entrée")
