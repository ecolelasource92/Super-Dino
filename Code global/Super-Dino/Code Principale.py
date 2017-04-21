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
#on définit les constante du jeu à 1 tant que le jeu tourne
continuer = 1

choix = 1

#Afficher l'écran d'accueil

image_accueil = pygame.image.load(fond).convert()
fenetre.blit(image_accueil,(0,0))

while continuer:
    #On définie les boucles du jeu
    #Une boucle pour l'interface d'accueil et une pour le niveau
    continuer_accueil = 1
    continuer_jeu = 1

    #BOUCLE D'ACCUEIL
    while continuer_accueil:
        pygame.time.Clock().tick(30)
        
        #fonction quitter qui met les constantes à 0 si l'on ferme le jeu ou l'on perd
        quitter()

        #On charge l'image du bouton play
        jouer = pygame.image.load(boutonplay)
        fenetre.blit(jouer, (64,168))

        #On rafraichit les images avec les fonctions pygame
        pygame.display.update()
        pygame.display.flip()

        #Fonction pygame : on presse la barre espace, la boucle accueil se ferme et le niveau 1 est définit comme le choix
        if pygame.key.get_pressed == K_SPACE :
            continuer_acceuil = 0
            choix = niveau1

        #si le choix n'est pas nul (ici Niveau 1) on lance le niveau grâce à la class créée
        #On génère et on affiche le niveau
        if choix != 0 :
            niveau = Niveau(choix)
            niveau.generer()
            niveau.afficher(fenetre)
            
            
            

            


        
        
    
    
