# class pour les combattants
class Combattants: 
#   _init_
#       on enregistre les 4 valeurs genre name, pv, attaque, defense
    def __init__(self, name, pv, attaque, defense ):
    
#   est en vie le self    
#       si il est en vie alors voir si pv est superieur a 0
#       renvoie true si le combattant est vivant
#   
#   il perd des pv
    def perd_vie(self, pv):
#       calculer les degats apres defense
#       soustraire les degats 
#       si le pv est negatif alors le mettre a 0
# 
#   frapper 
    def frapper():
#       appeler perdre des pv de la cible avec son attaque 