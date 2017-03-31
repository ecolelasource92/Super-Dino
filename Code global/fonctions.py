import pygame
from pygame.locals import *

#definition des constantes du jeu
def quitter() :
#Si l'utilisateur quitte, on met les variables 
#de boucle à 0 pour n'en parcourir aucune et fermer
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                continuer = 0
                continuer_accueil = 0
                continuer_jeu = 0

titrejeu = "Super Dino"
fond = 'images/interfacebeta.jpg'
boutonplay = 'images/startgame.png'
niveau1 = 'niveau1.txt'
perso = 'images/dinoavant.png', 'images/dinoretour.png'








