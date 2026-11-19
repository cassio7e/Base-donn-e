class Combattants: 

    def __init__(self, name, hp, attaque, defense ):
        self.name = name
        self.hp = hp
        self.attaque = attaque
        self.defense = defense
     
    def est_en_vie(self):
        return self.hp > 0
    
    def perd_pv(self, quantite):
        self.hp -= quantite
        degats = max(1, quantite - (self.defense //2))
        self.hp = max(0, self.hp - degats)

    def frapper(self, cible):
        degats = max(1, self.attaque - (cible.defense //2))
        cible.perd_pv(degats)
        return degats 
    
class Joueur(Combattants):
    pass

class Adversaire(Combattants):
    pass