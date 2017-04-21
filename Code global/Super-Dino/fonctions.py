import pygame
from pygame.locals import *

#definition des constantes du jeu

def quitter() :
#Si l'utilisateur quitte, on met les variables de boucle à 0 pour n'en parcourir aucune et fermer
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                continuer = 0
                continuer_accueil = 0
                continuer_jeu = 0
                choix = 0

#constantes accueil
titrejeu = "Super Dino"
fond = 'images/interfacebeta.jpg'
boutonplay = 'images/startgame.png'

#fichier niveau 1
#niveau1 = 'C:\Users\iness\Documents\GitHub\Screwed-Project\Super-Dino\niveau\niveau1.txt'

#constantes niveau
perso = 'images/dinoavant.png', 'images/dinoretour.png'
plateforme = 'images/mur.png'
arrivee = 'images/arrivee.png'
depart = 'images/depart.png'


#definition des sprites

nbspritelongueur = 60
taillesprite = 30
cotefenetre = taillesprite * nbspritelongueur

class Niveau : 

    def __init__(niveau1, fichier):
        niveau1.fichier = fichier
        niveau1.structure = 0

    def generer(niveau1) :
        with open('C:\Users\iness\Documents\GitHub\Screwed-Project\Super-Dino\niveau\niveautest.txt', "r") as fichier :
        #on définit notre fichier comme une liste
            structureniveau = []
            #on créé une liste par ligne du fichier
            for ligne in fichier :
                ligne_niveau = []
                for sprite in ligne :
                #on créé un sprite pour chaque lettre de la ligne en ignorant les retours à la ligne '\n'
                    if sprite != '\n' :
                        ligne_niveau.append(sprite)
                structureniveau.append(ligne_niveau)
            niveau1.structure = structureniveau

    def afficher(niveau1, fenetre):
        image_accueil = pygame.image.load(fond).convert()
        fenetre.blit(image_accueil,(0,0))
        
        plateforme = pygame.image.load(plateforme).convert()
        depart = pygame.image.load(depart).convert()
        arrivee = pygame.image.load(arrivee).convert_alpha()
		
        #On parcourt la liste du niveau
        num_ligne = 0
        for ligne in self.structure:
        #On parcourt les listes de lignes
            num_case = 0
            for sprite in ligne:
                #On calcule la position réelle en pixels
                x = num_case * taillesprite
                y = num_ligne * taillesprite
                if sprite == '0':		   #0 = Plateforme
                    fenetre.blit(plateforme, (x,y))
                elif sprite == 'V':		   #V = Départ
                    fenetre.blit(depart, (x,y))
                elif sprite == 'X':		   #X = Arrivée
                    fenetre.blit(arrivee, (x,y))
                num_case += 1
            num_ligne += 1



        
                        
                    
                    
            
            
            
    













