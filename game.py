import random 
import time
from models import Combattants, Joueur, Adversaire 
from utils import * 
from db_init import ENNEMIS
import utils
import shutil




def afficher_titre_encadre(texte):
    largeur = shutil.get_terminal_size().columns
    print(texte.center(largeur))


def formater_hero(heros_disponibles):
    liste = []
    for heros in heros_disponibles:
        string = f"{heros["name"]}, Attaque: {heros["attaque"]}, Defense: {heros["defense"]}, Hp: {heros["hp"]}"
        liste.append(string)
    return liste


def afficher_equipe(equipe):
    for c in equipe:
        print(f"{c.name}, Attaque: {c.attaque}, Defense: {c.defense}, Hp: {c.hp}")


def afficher_evenement(numero, adversaires):
    afficher_titre_encadre(f" Manche {numero}")
    afficher_titre_encadre ("Adversaires :")
    for adv in adversaires:
        print(f"- {adv.name},  ATK: {adv.attaque},  DEF: {adv.defense},  HP: {adv.hp}")    

       
def afficher_resultat_manche(gagnee):
    if gagnee: 
        print("-----Manche gagné----- ")
    else: 
        print("------Manche perdu------")


def afficher_score_final(score):
    print(f"-----La Partie est terminée. Vous avez gagné {score} manche-----")


def demander_pseudo():
    pseudo = input("-----Entre ton pseudo :-----")
    return pseudo 


def creation_equipe(heros_disponibles):
    equipe = []
    phrases_heros = formater_hero(heros_disponibles)
    while len(equipe) < 3:
        index = recuperer_choix_valide(phrases_heros)
        hero_data = heros_disponibles[index - 1]
        nouveau_joueur = Joueur(hero_data['name'], hero_data['hp'], hero_data['attaque'], hero_data['defense'])
        equipe.append(nouveau_joueur)
    return equipe 


       
def equipe_en_vie(combattants): 
    for c in combattants:     
        if c.est_en_vie():
            return True
    return False 


def choisir_cible_vivante(cibles):
    vivants = [c for c in cibles if c.est_en_vie()]
    return random.choice(vivants)

def deroulement_manche(equipe, adversaires):
    while equipe_en_vie(equipe) and equipe_en_vie(adversaires):
        phase_attaque(equipe, adversaires)
        if not equipe_en_vie(adversaires):
            return True      
        phase_attaque(equipe, adversaires)
        if not equipe_en_vie(equipe):
            return False 
    return equipe_en_vie(equipe)


def phase_attaque(attaquants, defenseurs):
    for attaquant in attaquants: 
        if attaquant.est_en_vie() and equipe_en_vie(defenseurs):
            cible = choisir_cible_vivante(defenseurs)
            attaquant.frapper(cible)



def choisir_random_ennemis(ennemis_disponible):
    ennemis_disponible_copy = ennemis_disponible.copy()
    adversaires = []
    for _ in range(3):
        adv_data = random.choice(ennemis_disponible_copy)
        adversaires.append(Adversaire(adv_data['name'], adv_data['attaque'],adv_data['defense'],adv_data['hp']))
        ennemis_disponible_copy.remove(adv_data)
    return adversaires


def lancer_partie():
    pseudo = demander_pseudo()
    heros_disponibles = utils.charger_heros()
    equipe = creation_equipe(heros_disponibles)
    afficher_equipe(equipe)
    score = 0
    ennemis_disponible = utils.charger_ennemis()
    while equipe_en_vie(equipe):
        adversaires = choisir_random_ennemis(ennemis_disponible)     
        afficher_evenement(score + 1, adversaires)
        gagnee = deroulement_manche(equipe,adversaires)
        if gagnee:
            score += 1
        afficher_resultat_manche(gagnee)
    utils.enregistrer_partie(pseudo, score) 
    afficher_score_final(pseudo, score)
