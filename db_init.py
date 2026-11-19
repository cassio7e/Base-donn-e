from pymongo import MongoClient 



HEROS = [
    {"name": "Leonardo", "attaque": 14, "defense": 10, "hp": 120},
    {"name": "Raphael", "attaque": 13, "defense": 13, "hp": 120},
    {"name": "Donatello", "attaque": 20, "defense": 9, "hp": 120},
    {"name": "Michelangelo", "attaque": 12, "defense": 20, "hp": 120},
]

ENNEMIS = [
    {"name": "Shredder", "attaque": 11, "defense": 21, "hp": 120},
    {"name": "Krang", "attaque": 13, "defense": 13, "hp": 120},
    {"name": "Bebop", "attaque": 15, "defense": 10, "hp": 120},
    {"name": "Lord Dregg", "attaque": 22, "defense": 20, "hp": 120},
]


# preparer_base()
def preparer_base():
    # se connecter au serveur MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["arene_rpg"]
    # compter les documents dans la collection heros
    # si aucun héros, appeler reinitialiser_base
    if db.heros.count_documents({}) == 0:
    # fermer la connexion
        reinitialiser_base()
#   garantit que la base contient les données nécessaires au jeu
    client.close()
    
    
        
    

# reinitialiser la base (donc remte l'arene dans l'état de base)
def reinitialiser_base():
#   se connecter a la base 
    client = MongoClient("mongodb://localhost:27017/")
    db = client["arene_rpg"]
#   supprimer les collections heros, ennemis et score
    db.heros.drop()
    db.ennemis.drop()
    db.palmares.drop()
#   définir les liste de heros et ennemis dans leur propre collection du meme nom
    db.heros.insert_many(HEROS)
    db.ennemis.insert_many(ENNEMIS)
#   fermer la connexion  
    client.close()
