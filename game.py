
#  afficher les personnages et leurs caracteristiques
def afficher_heros_disponibles(heros_disponibles):
#   parcourir une liste tout en gardant un numéro automatique pour chaque élément.
    for i, h in enumerate(heros_disponibles, start=1):
#       afficher f"{index}. {h['name']} (ATQ {h['attack']}, DEF {h['defense']}, PV {h['hp']})")"
        print(f"{i}. {h['name'], Attaque: {h['attaque']}, Defense:  {h['defense']}, hp:  {h['hp']} }")
 
# afficher_equipe
#   parcourir les membres de l'equipe et afficher leurs infos

# afficher l'evenement du match


def afficher_evenement(numero, adversaire):
#   afficher le numero de manche 
    print(f" Manche 1")
#   afficher les adversaire
#       pour adv(adversiare) dans adversaire
#           print(f"- {adv.name} | ATK: {adv.attack} | DEF: {adv.defense} | HP: {adv.hp}")    
       
#afficher le score final 
    afficher le pseudo et le score 

# demander le pseudo
def demander_pseudo():
#   demander et retourner le pseudo
    pseudo = input("Entre ton pseudo :")
    return pseudo 
#
# demander le choix heros(choisir un personnage sur la liste)---> ou est ce qeu j'ai mis "les personnage sur la liste" 
def choix_heros():
#   pendant que c'est Vrai    
    while True: 
#        afficher chaque personnage numéroté 
         afficher_heros_disponibles(heros_disponible)
#       demander de choisir un numero valide 
        saisie = input("Choisi le numéro d'un héros :")
#       si le choix est invalide ou déjà pris, afficher une erreur et recommencer
        if utils.est choix_valide(saisie, 1, len(heros_disponibles)):
#           retourner le choix dans l'index choisi
            index = int(saisie) - 1
            hero = heros_disponibles[index]
            # si pas deja pris  retourner a l'index 
            if not deja_pris: 
                return index 
            else : 
                print("Ce heros est deja dans l'equipe")
        else:
        print("Choix invalide")

        
#   
#
# creation de l'equipe (personnage_disponibles)
def creation_equipe(heros_disponible):
#   initialiser une equipe vide
    equipe = []
#    repeter tant que avoir 1 a lend personnages (3)
    while len(equipe) < 3:
#       choisir un heros VALIDE
        index = choix_heros(heros_disponible, equipe)
        hero_data = heros_disponible[index]
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
    vivants = [c for c in combattants if c.est_en_vie()]
#   choisir au hasard
#   retouner le hero choisi 
    return random.choice(vivants)
#

# deroulement manche
#   tant que les deux equipes ont des vivants 
#       chaque heros vivant attaque un adversaire vivant
#           Si le heros est en vie 
#               heros choisi une cible vivante 
#               frappe avec un temps de 1
#       Si tous les adversaires sont mort, la manche est gagné 
#           chaque adversaire vivant attaque un heros vivant
#   l'équipe des heros gagne si il en reste un au moins en vie 

# 

#
# lancer partie COMPLETE
def lancer_partie():
#   demande du pseudo
#   charger les heros
#   creer l'equipe hero
#   mettre le score de base a 0
#   charger les ennemis
#   tant que l'équipe heros est en vie 
#       choisir 3 ennemis random
#       creer instance Adversaire 
#       afficher la manche 
#       deroulement de la manche 
#       si la manche est gagné alors augmenter le score 
#       afficher le score 
#       temps de pause av score
#   enregistrer le score et afficher le resultat 
#   afficher le score final 
#



