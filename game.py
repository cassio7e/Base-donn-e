
#  afficher les personnages et leurs caracteristiques
def afficher_heros_disponibles(heros_disponibles):
#   parcourir une liste tout en gardant un numéro automatique pour chaque élément.
    for i, h in enumerate(heros_disponibles, start=1):
#       afficher f"{index}. {h['name']} (ATQ {h['attack']}, DEF {h['defense']}, PV {h['hp']})")"
        print(f"{i}. {h['name'], Attaque: {h['attaque']}, Defense:  {h['defense']}, hp:  {h['hp']} }")
# 
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
       #   afficher chaque personnage numéroté 
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

#     
# choisir un monstre disponible
def choisir_monstre(): 
#   choisir un monstre au hasard
#   creer un adversaire 
#    
#
# Pour faire attaquer tous les personnages vivants
def attaque_perso():
#   evenements vide 
#    pour chaque joueurs vivant dans le'equipe 
#       si le joueur est en vie et le monstre est en vie
#           le joueur attaque le monstre 
#       si le monstre n'est plus en vie 
#           on a tuer le monstre 
#           break
#       
#
# choisir un personnage vivant en cible aléatoire 
def choisir_cible_vivante():
#   lister les vivants
    vivants = [c for c in combattants if c.est_en_vie()]
#   choisir au hasard
#   retouner le hero choisi 
    return random.choice(vivants)
#
#
# attaque du monstre 
def attaque_monstres():
#   choisir un personnage vivant 
#   le monstre attaque 
#   mettre un message si le perso est mort 
#
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
#
# afficher l'evenement
def afficher_evenement():
#   afficher le message recu
#   affiche un message de combat
#
# afficher tous les messages d'un tour
def afficher_message():
#   afficher chaque message
# 
# afficher l'etat de l'equipe
def etat_equipe():
#   affichez un texte de presentation 
#   affichez chaque personnage en vie 
# 
# afficher le score final
def score_final(): 
#   afficher le pseudo et le nombre de manches a gagnees
# 
# combattre le monstre
def combattre_monstre(): 
#   tant que le monstre et equipe en vie 
#       equipe attaque puis monnstre attque 
#   afficher l'évenement
#
# 
# boucle du jeux 
def boucle_jeux():
#   score de base =0
#   tant que equipe est en vie 
#       choisir le monstre
#       afficher texte avec le nom du monstre
#       combattre le monstre 
#   si le monstre est mort 
#       on augmente le score 
#
#
# lancer partie COMPLETE
def lancer_partie():
#   demande du pseudo
#   charger les personnages
#   creer une equipe 
#   lancer la boucle de jeu
#   enregistrer le score et afficher le resultat 
#
#
# lancer le score des meilleurs joueurs
def lancer_score():
    print ("Voici le tableau des SCORES")
#   texte SCORES
#   Si pas de score alors message vide 
#   sinon afficher chaque score 
#
#




