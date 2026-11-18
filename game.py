import random 
import time
from models import Combattants, Joueur, Adversaire 
import utils 


#  afficher les personnages et leurs caracteristiques
def afficher_heros_disponibles(heros_disponibles):
#   parcourir une liste tout en gardant un numéro automatique pour chaque élément.
    for i, h in enumerate(heros_disponibles, start=1):
#       afficher f"{index}. {h['name']} (ATQ {h['attack']}, DEF {h['defense']}, PV {h['hp']})")"
        print(f"{i}. {h['name']}, Attaque: {h['attaque']}, Defense:  {h['defense']}, hp:  {h['hp']} ")


 
# afficher_equipe
def afficher_equipe(equipe):
#   parcourir les membre de l'equipe et mettre leur infos avec un numero 
    for c in equipe:
        print(f"{c.name}, Attaque: {c.attaque}, Defense: {c.defense}, Hp: {c.hp}")

def afficher_heros_disponibles(heros_disponibles):
#   parcourir les membres de l'equipe et afficher leurs infos
    for i, h in enumerate(heros_disponibles, start=1):
        print(f"{i}. {h['name']} | Attaque: {h['attaque']} | Defence: {h['defense']} | Hp: {h['hp']}")


# afficher l'evenement du match
def afficher_evenement(numero, adversaires):
#   afficher le numero de manche 
    print(f" Manche {numero}")
#   afficher les adversaire
    print ("Adversaires :")
#   pour adv(adversiare) dans adversaire
    for adv in adversaires:
#       print(f"- {adv.name} | ATK: {adv.attack} | DEF: {adv.defense} | HP: {adv.hp}")    
        print(f"- {adv.name} | ATK: {adv.attack} | DEF: {adv.defense} | HP: {adv.hp}")    

       
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


# demander le choix heros(choisir un personnage sur la liste)---> ou est ce qeu j'ai mis "les personnage sur la liste" 
def choix_heros(heros_disponibles, equipe):
#   pendant que c'est Vrai    
    while True: 
#       afficher chaque personnage numéroté 
        afficher_heros_disponibles(heros_disponibles)
#       demander de choisir un numero valide 
        saisie = input("Choisi le numéro d'un héros :")
#       si le choix est invalide ou déjà pris, afficher une erreur et recommencer
        if utils.est_choix_valide(saisie, 1, len(heros_disponibles)):
#           retourner le choix dans l'index choisi
            index = int(saisie) - 1
            hero = heros_disponibles[index]
            # si pas deja pris  retourner a l'index 
            deja_pris = any (c.name == hero ['name'] for c in equipe)
            if not deja_pris: 
                return index 
            else : 
                print("Ce heros est deja dans l'equipe")
        else:
            print("Choix invalide")

        
#   
#
# creation de l'equipe (personnage_disponibles)
def creation_equipe(heros_disponibles):
#   initialiser une equipe vide
    equipe = []
#    repeter tant que avoir 1 a lend personnages (3)
    while len(equipe) < 3:
#       choisir un heros VALIDE
        index = choix_heros(heros_disponibles, equipe)
        hero_data = heros_disponibles[index]
#       creer l'instance Joeur et la mettre dans equipe
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
def choisir_cible_vivante():
#   lister les vivants
    vivants = [c for c in Combattants if c.est_en_vie()]
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
#           Si le heros est en vie il devient une cible vivante 
            cible = choisir_cible_vivante(adversaires)
#               frappe avec un temps de 1
            hero.frapper(cible)
            time.sleep(1)
#       Si tous les adversaires sont mort, la manche est gagné
        if not equipe_en_vie(adversaires):
            break
#           chaque adversaire vivant attaque un heros vivant
        for adv in adversaires:
            if adv.est_en_vie():
                cible = choisir_cible_vivante(equipe)
                adv.frapper(cible)
                time.sleep(1)
#   l'équipe des heros gagne si il en reste un au moins en vie 
    return equipe_en_vie(equipe)

# 

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
#       choisir 3 ennemis random
        adversaires = []
        for _ in range(3):
            adv_data = random.choice(ennemis_disponible)
#           creer instance Adversaire 
            adversaires.append(Adversaire(adv_data['name'], adv_data['attaque'],adv_data['defense'],adv_data['hp']))
#       afficher la manche
        afficher_evenement(score + 1, adversaires)
#       deroulement de la manche
        gagnee = deroulement_manche
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
