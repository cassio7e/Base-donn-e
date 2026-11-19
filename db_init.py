from pymongo import MongoClient 



HEROS = [
    {"name": "Leonardo", "attaque": 140, "defense": 10, "hp": 12000000},
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


def preparer_base():
        client = MongoClient("mongodb://localhost:27017/")
        db = client["arene_rpg"]
        if db.heros.count_documents({}) == 0:
            reinitialiser_base()
        client.close()
    
    
        
    

def reinitialiser_base():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["arene_rpg"]
    db.heros.drop()
    db.ennemis.drop()
    db.palmares.drop()
    db.heros.insert_many(HEROS)
    db.ennemis.insert_many(ENNEMIS)
    client.close()

preparer_base()