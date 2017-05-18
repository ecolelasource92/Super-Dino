import pygame
from pygame.locals import *
from fonctions import *

pygame.init()

    
#PROGRAMME PRINCIPALE

#Initialisation Interface

LongueurInterface = 640
LargeurInterface = 480
fenetre = pygame.display.set_mode((LongueurInterface, LargeurInterface), RESIZABLE)
newposition = 0
                                  
#Titre fenetre
pygame.display.set_caption(titrejeu)

# initialisation des booléens pour afficher la banane
mangerbanane = passage = False


#BOUCLE PRINCIPALE
#on définit les constante du jeu à 1 tant que le jeu tourne
continuer = 1
choix = 1

#Afficher l'Ã©cran d'accueil

image_accueil = pygame.image.load(fond).convert()
fenetre.blit(image_accueil,(0,0))

# chargement des sons
sonaccueil =  pygame.mixer.Sound("sons/Mriodie.wav")
sontouche = pygame.mixer.Sound("sons/Jump.wav")
sonmiam = pygame.mixer.Sound("sons/Stage Clear.wav")
# on defini le volume
sonaccueil.set_volume(0.5)   # HP à 50%
sontouche.set_volume(0.3)   # HP à 30%
sonmiam.set_volume(0.5)   # HP à 50%

while continuer:
    #On définie les boucles du jeu
    #Une boucle pour l'interface d'accueil et une pour le niveau
    continuer_accueil = 1
    continuer_jeu = 1

    #BOUCLE D'ACCUEIL
    while continuer_accueil == 1 :
        pygame.time.Clock().tick(30)
        sonaccueil.play()
        #fonction quitter qui met les constantes à  0 si l'on ferme le jeu ou l'on perd
        quitter()


        #On rafraichit les images avec les fonctions pygame
        pygame.display.update()
        pygame.display.flip()


        #Fonction pygame : on presse la barre espace, la boucle accueil se ferme et le niveau 1 est dÃ©finit comme le choix

        if pygame.key.get_pressed()[pygame.K_SPACE] :
                continuer_accueil = 0
                choix = 'niveau/niveau1.txt'
                

        #si le choix n'est pas nul (ici Niveau 1) on lance le niveau gràce à  la class créee
        #On génère et on affiche le niveau
                if choix != 0 :
                    
                    niveau = Niveau(choix)
                    niveau.generer()
                    niveau.afficher(fenetre)                    
                    pygame.display.update()
                    pygame.display.flip()
                  
                   
                    perso = pygame.image.load("images/base_droite.png").convert_alpha()
                    perso_rect = perso.get_rect() #on crée un rectangle entourant l'image
                    perso_rect = perso_rect.move (0,+270) #on place Dino au début de la Plate forme 
                    
                    fenetre.blit(perso, perso_rect) #on blitte l'image dans ce rectangle
                    
                    #on affiche les bananes au démarrage
                    banane = pygame.image.load("images/arrivee.png").convert_alpha()
                    fenetre.blit(banane,(300,200)) #on place la banane au centre
                    
                    pygame.key.set_repeat(10, 10) #on active la répétition des touches
                                    
                    while 1:
                        pygame.time.Clock().tick(30)
                        # Les commandes d'action
                        for e in pygame.event.get():    #on boucle à l'infinie sur l'evenement GET KEY
                            if e.type == KEYDOWN and e.key == K_UP:
                                sontouche.play()
                                perso_rect = perso_rect.move (0,-10)
                                perso = pygame.image.load("images/base_droite.png").convert_alpha()
                            if e.type == KEYDOWN and e.key == K_DOWN:
                                sontouche.play()
                                #Dino ne doit pas decendre sous les blocs
                                if not (perso_rect.y >= 270 and (perso_rect.x <=370 or perso_rect.x >460)):
                                    perso_rect = perso_rect.move (0,+10)
                                    perso = pygame.image.load("images/base_droite.png").convert_alpha()                           
                                else :
                                    pass
                            if e.type == KEYDOWN and e.key == K_LEFT:
                                sontouche.play()
                                perso_rect = perso_rect.move (-10,0)
                                perso = pygame.image.load("images/base_gauche.png").convert_alpha()
                            if e.type == KEYDOWN and e.key == K_RIGHT:
                                sontouche.play()
                                perso_rect = perso_rect.move (+10,0)
                                perso = pygame.image.load("images/base_droite.png").convert_alpha()
                            if e.type == KEYDOWN and e.key == K_SPACE:
                                sontouche.play()
                                perso_rect = perso_rect.move (+25,0)
                                perso = pygame.image.load("images/base_droite.png").convert_alpha()
                                
                            # game over par la touche Escape ou la fermeture de fenetre par clic souris
                            if e.type == KEYDOWN and e.key == K_ESCAPE:
                                raise SystemExit
                            if e.type == pygame.QUIT: #fonction quitter par la croix
                                pygame.quit()

                            #affichage de la nouvelle position de dino
                            #print ("perso rect", perso_rect)
                            fenetre.blit(perso,perso_rect)
                            pygame.display.update()                            
                            
                            #on efface l'encienne position en redessinant le fond
                            niveau.generer()
                            niveau.afficher(fenetre)

                            #on affiche les bananes si dino ne les a pas mangées
                            positiondino = perso_rect
      
                            if positiondino == (280, 180, 67, 66): # si Dino est sur la banane
                                mangerbanage = True                # il mange la banane
                                passage = True                     # on memorise son passage pour ne plus afficher la banane
                                sonmiam.play()
                                print "miam"
                            elif passage == False:
                                mangerbanane == False
                                #print "pas manger"
                                banane = pygame.image.load("images/arrivee.png").convert_alpha()
                                fenetre.blit(banane,(300,200))
                                           
                            #delai de 3000ml pour debug
                            #pygame.time.delay(3000)

                          

                        
