# class pour les combattants
class Combattants: 
#   _init_

    def __init__(self, name, hp, attaque, defense ):
#       initailisation 'un combattant avec nom et info
        self.name = name
        self.hp = hp
        self.attaque = attaque
        self.defense = defense
     
#   est en vie le self 
    def est_en_vie(self):
#       renvoie true si pv du combattant sont positive (strictement)
        return self.hp > 0
    
#   il perd des pv
    def perd_pv(self, quantite):
#       réduire les points de vie de la quantité de degat reçue
        self.hp -= quantite
#       soustraire au hp sans descendre sous 0
        degats = max(1, quantite - (self.defense //2))
        self.hp = max(0, self.hp - degats)

#   frapper 
    def frapper(self, cible):
#       cacule des degats avec des resulats entier
        degats = max(1, self.attaque - (cible.defense //2))
#       la cible prend des degats
        cible.perd_pv(degats)
#       retourner le resultat des dégats infligés a la cible 
        return degats 
    
#Classe joueur (combatant)
class Joueur(Combattants):
    pass

#Classe adversaire (combatant)
class Adversaire(Combattants):
    pass