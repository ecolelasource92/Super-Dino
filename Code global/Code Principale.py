import pygame
from pygame.locals import *
from fonctions import *

pygame.init()



#MOUSEBUTTONDOWN signifie le clique, button 1 le bouton gauche
#event.pos[0] = position abscisse et event.pos[1] = position ordonnée
    
    
#PROGRAMME PRINCIPALE

#Initialisation Interface

LongueurInterface = 640
LargeurInterface = 480
fenetre = pygame.display.set_mode((LongueurInterface, LargeurInterface), RESIZABLE)


#Titre fenêtre
pygame.display.set_caption(titrejeu)


#BOUCLE PRINCIPALE
continuer = 1

#Afficher l'écran d'accueil

image_accueil = pygame.image.load(fond).convert()
fenetre.blit(image_accueil,(0,0))

while continuer:
    #On définie les boucles du jeu
    continuer_accueil = 1
    continuer_jeu = 1

    #BOUCLE D'ACCUEIL
    while continuer_accueil:
        quitter()
        
        jouer = pygame.image.load(boutonplay)
        fenetre.blit(jouer, (64,168))

        pygame.display.update()
        pygame.display.flip()


        
        
    
    