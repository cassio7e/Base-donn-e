import random 
import time
from models import Combattants, Joueur, Adversaire 
from utils import * 
from db_init import ENNEMIS
import utils



#formater_hero(hero_disponible)
def formater_hero(heros_disponibles):
#   fait une liste    
    liste = []
#    pour chaque hero
    for heros in heros_disponibles:
#        ajouter a la liste une chaine de caractere avec ses info
        string = f"{heros["name"]}, Attaque: {heros["attaque"]}, Defense: {heros["defense"]}, Hp: {heros["hp"]}"
        liste.append(string)
#   return liste  
    return liste


# afficher_equipe
def afficher_equipe(equipe):
#   parcourir les membre de l'equipe et mettre leur infos avec un numero 
    for c in equipe:
        print(f"{c.name}, Attaque: {c.attaque}, Defense: {c.defense}, Hp: {c.hp}")




# afficher l'evenement du match
def afficher_evenement(numero, adversaires):
#   afficher le numero de manche 
    print(f" Manche {numero}")
#   afficher les adversaire
    print ("Adversaires :")
#   pour adv(adversiare) dans adversaire
    for adv in adversaires:
#       print(f"- {adv.name} | ATK: {adv.attack} | DEF: {adv.defense} | HP: {adv.hp}")    
        print(f"- {adv.name} | ATK: {adv.attaque} | DEF: {adv.defense} | HP: {adv.hp}")    

       
#afficher le score de la manche
def afficher_resultat_manche(gagnee):
#   si gagner alors afficher un mess de victoire
    if gagnee: 
        print("Manche gagné ")
#   sinon message de defaite
    else: 
        print("Manche perdu ")

#afficher le score final 
def afficher_score_final(pseudo, score):
#   afficher mess final avec le pseudo et le score
    print(f" La Partie est terminée. Vous avez gagné {score} manche")

# demander le pseudo
def demander_pseudo():
#   demander et retourner le pseudo
    pseudo = input("Entre ton pseudo :")
    return pseudo 
#
#
# creation de l'equipe (personnage_disponibles)
def creation_equipe(heros_disponibles):
#   initialiser une equipe vide
    equipe = []
#   Bien former les infos brutes
    phrases_heros = formater_hero(heros_disponibles)
#   repeter tant que avoir 1 a lend personnages (3)    
    while len(equipe) < 3:
#       choisir un heros VALIDE
        index = recuperer_choix_valide(phrases_heros)
        hero_data = heros_disponibles[index - 1]
#       creer l'instance Joueur et la mettre dans equipe
        nouveau_joueur = Joueur(hero_data['name'], hero_data['hp'], hero_data['attaque'], hero_data['defense'])
        equipe.append(nouveau_joueur)
#    return   
    return equipe 


       
# equipe en vie 
def equipe_en_vie(combattants): 
#   parcourrir la liste des combattants
    for c in combattants:     
#       verifier si au moins un des heros est vivant
        if c.est_en_vie():
#           retourne true 
            return True
#   sinon retourner False
    return False 


# choisir un personnage vivant en cible aléatoire 
def choisir_cible_vivante(cibles):
#   lister les vivants
    vivants = [c for c in cibles if c.est_en_vie()]
#   choisir au hasard
#   retouner le hero choisi 
    return random.choice(vivants)
#

# deroulement manche
def deroulement_manche(equipe, adversaires):
#   tant que les deux equipes ont des vivants
    while equipe_en_vie(equipe) and equipe_en_vie(adversaires):
#       chaque heros vivant attaque un adversaire vivant
        for hero in equipe:
#           Si le heros est en vie il devient une cible vivante, on arrète la phase d'attaque 
            if hero.est_en_vie():
                cible = choisir_cible_vivante(adversaires)
#               frappe avec un temps de 1
                hero.frapper(cible)
                time.sleep(1)
#            Si tous les adversaires sont mort, la manche est gagné
            if not equipe_en_vie(adversaires):
#               return vrai (mache gagnée)
                return True 
#               chaque adversaire vivant attaque un heros vivant
            for adv in adversaires:
                if adv.est_en_vie():
                    cible = choisir_cible_vivante(equipe)
                    adv.frapper(cible)
                    time.sleep(1)
#   Verifier que tous les geros sont morts 
    if not equipe_en_vie(equipe):
#       retourne que la manche est perdu 
        return False 

# choisir random ennemis
def choisir_random_ennemis(ennemis_disponible):
#   choisir random ennemis
    ennemis_disponible_copy = ennemis_disponible.copy()
    adversaires = []
    for _ in range(3):
#       choisir un heros VALIDE
        adv_data = random.choice(ennemis_disponible_copy)
#       creer instance Adversaire 
        adversaires.append(Adversaire(adv_data['name'], adv_data['attaque'],adv_data['defense'],adv_data['hp']))
        ennemis_disponible_copy.pop()
    return adversaires
#
# lancer partie COMPLETE
def lancer_partie():
#   demande du pseudo
    pseudo = demander_pseudo()
#   charger les heros
    heros_disponibles = utils.charger_heros()
#   creer l'equipe hero
    equipe = creation_equipe(heros_disponibles)
    afficher_equipe(equipe)
#   mettre le score de base a 0
    score = 0
#   charger les ennemis
    ennemis_disponible = utils.charger_ennemis()
#   tant que l'équipe heros est en vie 
    while equipe_en_vie(equipe):
        adversaires = choisir_random_ennemis(ENNEMIS)     
#       afficher la manche
        afficher_evenement(score + 1, adversaires)
#       deroulement de la manche
        gagnee = deroulement_manche(equipe,adversaires)
#       si la manche est gagné alors augmenter le score 
        if gagnee:
            score += 1
#       afficher le score
        afficher_resultat_manche(gagnee)
#       temps de pause av score
        time.sleep(1)
#   enregistrer le score et afficher le resultat
    utils.enregistrer_partie(pseudo, score) 
#   afficher le score final 
    afficher_score_final(pseudo, score)
