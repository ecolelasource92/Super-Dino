import pygame
from pygame.locals import *

#definition des constantes du jeu

def quitter():
#Si l'utilisateur quitte, on met les variables de boucle a 0 pour n'en parcourir aucune et fermer
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                continuer = 0
                continuer_accueil = 0
                continuer_jeu = 0
                choix = 0

#constantes accueil
titrejeu = "Super Dino"
fond = 'images/interfacebeta.jpg'
fondniveau = 'images/interfaceniveau.png'



#fichier niveau 1
#niveau1 = 'C:\Users\iness\Documents\GitHub\Screwed-Project\Super-Dino\niveau\niveau1.txt'

#constantes niveau
#perso = 'images/dinoavant.png', 'images/dinoretour.png'



#definition des sprites
nbsprite = 61
taillesprite = 55
hauteurfenetre = taillesprite * nbsprite

class Niveau : 

    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = 0

    def generer(self) :
        with open('niveau/niveau1.txt', "r") as fichier :
        #on definit notre fichier comme une liste
            structureniveau = []
            #on cree une liste par ligne du fichier
            for ligne in fichier :
                ligne_niveau = []
                for sprite in ligne :
                #on un sprite pour
                    if sprite != '\n' :
                        ligne_niveau.append(sprite)
                structureniveau.append(ligne_niveau)
            self.structure = structureniveau

    def afficher(self, fenetre):
        imageniveau = pygame.image.load(fondniveau).convert()
        fenetre.blit(imageniveau, (0,0))
        
        plateforme1 = pygame.image.load('images/plateform1.png').convert()
        plateforme2 = pygame.image.load('images/plateform4.png').convert()
        plateforme3 = pygame.image.load('images/plateform6.png').convert()
        plateforme4 = pygame.image.load('images/plateform9.png').convert()
        plateforme5 = pygame.image.load('images/plateform2.png').convert()
        plateforme6 = pygame.image.load('images/plateform7.png').convert()
        plateforme = pygame.image.load('images/plateform5.png').convert()
        arrivee = pygame.image.load('images/arrivee.png').convert()
        perso = pygame.image.load('images/base_droite.png').convert()
        
		
        #On parcourt la liste du niveau
        num_ligne = 0
        for ligne in self.structure:
        #On parcourt les listes de lignes
            num_case = 0
            for sprite in ligne:
                #On calcule la position reelle en pixels
                x = num_case * taillesprite
                y = num_ligne * taillesprite
                if sprite == 'O':		   #0 = Plateforme
                    fenetre.blit(plateforme, (x,y))
                elif sprite == '1' :
                    fenetre.blit(plateforme1, (x,y))
                elif sprite == '2' :
                    fenetre.blit(plateforme2, (x,y))
                elif sprite == '3' :
                    fenetre.blit(plateforme3, (x,y))
                elif sprite == '4' :
                    fenetre.blit(plateforme4, (x,y))
                elif sprite == '5' :
                    fenetre.blit(plateforme5, (x,y))
                elif sprite == '6' :
                    fenetre.blit(plateforme6, (x,y))
                elif sprite == 'A':		   #X = Arrivee
                    fenetre.blit(arrivee, (x,y))
                num_case += 1
            num_ligne += 1

        
                        
                    
                    
            
            
            
    













