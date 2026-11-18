# charger les heros 
def charger_heros():
#   se brancher a la base 
#   récuperer tous les documents dans la collection heros 
#   les mettre dans une liste
#   retourner la liste 
# 
# charger les ennemis 
def charger_ennemis():
#   se brancher a la base 
#   récuperer tous les documents dans la collection heros 
#   les mettre dans une liste
#   retourner la liste 
# 
# charger le palmares (renvoyer le classement des meilleurs scores)
def charger_score():
#   se brancher a la base 
#   recuperer tous les documents de la collection Scores
#   trier par nombre de manche decroissante
#   les mettre en liste
#   retourner la liste
# 
# enregistrer la partie (sauvegarde des resultats)
def enregistrer_partie():
#   se brancher a la base 
#   creer le doc avec le pseudo et le score 
#   inserer dans la collection Score

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