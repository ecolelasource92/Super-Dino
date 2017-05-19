import pygame
from pygame.locals import *
from Moteur_SUPERDINO2 import*



#Initialisation Interface d'accueil

LongueurInterface = 640
LargeurInterface = 480
fenetre = pygame.display.set_mode((LongueurInterface, LargeurInterface), RESIZABLE)

#constantes accueil

titrejeu = "Super Dino"
fond = 'images/interfacebeta.jpg'                              

#Titre fenêtre

pygame.init()
pygame.display.set_caption(titrejeu)

#Afficher l'écran d'accueil

image_accueil = pygame.image.load(fond).convert()
fenetre.blit(image_accueil,(0,0))
pygame.display.update()


#BOUCLE D'ACCUEIL

while 1 :
    pygame.time.Clock().tick(60)
    
    for event in pygame.event.get():    # Fonction Pygame de collecte d'information d'évènements
        if event.type == pygame.QUIT:   # Si l'évènement est la fermeture de la fenêtre
            pygame.quit()               # fermeture du jeu
            exit()
            
        if event.type == KEYDOWN and event.key == K_ESCAPE: # Si l'évènement est de presser échap
            pygame.quit()                                   # fermeture du jeu
            exit()
                    
        if event.type == KEYDOWN and event.key == K_SPACE:  # Si l'évènement est de presser espace
            main()                                          # on lance le jeu
     
    
       
