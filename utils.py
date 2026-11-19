from pymongo import MongoClient 
import shutil 
from game import afficher_titre_encadre

URL_MONGO = "mongodb://localhost:27017/"
NOM_BASE = "arene_rpg"



def afficher_nombre_disponibles(options, start=1):
    for i, o in enumerate(options, start=start):
        print(f"{i} : {o}")

def obtenir_connexion():
    client = MongoClient("mongodb://localhost:27017/")
    db = client[NOM_BASE]
    return db

def charger_heros():
    db = obtenir_connexion()
    heros =list(db.heros.find())
    return heros 


def charger_ennemis():
    db = obtenir_connexion()
    ennemis =list(db.ennemis.find())
    return ennemis


def charger_score():
    db = obtenir_connexion()
    score = list(db.scores.find({}, {"_id": 0}))
    return score


def enregistrer_partie(joueur, manches):
    db = obtenir_connexion()
    document = {"joueur": joueur, "manches": manches}
    db.palmares.insert_one(document)
    

def choix_valide(choix, min , max): 
    if not choix.isdigit():
        return False                      
    nombre = int(choix)
    return min <= nombre <= max



def recuperer_choix_valide(options):
    while True:
        afficher_nombre_disponibles(options, start = 1)        
        choix = input("Choisi une option :")
        if choix_valide(choix, 1, len(options)):
            return  int(choix)
        afficher_titre_encadre("Erreur")


def afficher_scores():
    scores = charger_score()
    if not scores:
        afficher_titre_encadre("Aucun score enregistré actuellement")
        return
    afficher_titre_encadre("----------SCORES----------")
    scores_tries = sorted(scores, key=lambda x:x['manches'], reverse=True)
    for rang, doc in enumerate(scores_tries[:3], start=1):
        print(f"{rang}. {doc['joueur']} - {doc['manches']} manches")
        input("Si tu veux revenir au menu appuis sur Entrée")
