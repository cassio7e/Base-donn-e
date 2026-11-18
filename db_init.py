# reinitialiser la base (donc remte l'arene dans l'état de base)
def reinitialiser_base():
#   se connecter a la base 
#   supprimer les collections heros, ennemis et score
#   définir les liste de heros et ennemis dans leur propre collection du meme nom 
#   fermer la connexion  



HERO = [
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
