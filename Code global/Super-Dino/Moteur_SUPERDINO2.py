import pygame
from pygame import *

# On définit ici les variables fondamentales, la demi largeur et hauteur serviront à la caméra

LargeurInterface = 640
HauteurInterface = 480
DemiLargeur = int(LargeurInterface / 2)
DemiHauteur = int(HauteurInterface / 2)

taille_perso = 65

#Chargement de l'écran

fenetre = pygame.display.set_mode((LargeurInterface, HauteurInterface))


'''

CLASSE PRIMMORDIALE DU JEU: la classe Entity

'''

# Ses caractéristiques:
# Elle hérite de la Classe pygame.sprite.Sprite, classe de base de Pygame (intégrée dans celui-ci) qui permet de créer un bloc visible du jeu (sprite)
# Autrement dit, la Classe Entity permet de créer les sprites, et est indispensable pour les autres classes du jeu qui créent des objets visibles

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 


'''

SECTION PRINCIPALE DU JEU : la fonction main()

'''

# La fonction main va regrouper l'ensemble de notre jeu. Pour lancer la partie, il ne suffira plus que d'écrire "main()".

def main():

    pygame.init()
    pygame.display.set_caption("SUPER DINO V2")
    horloge = pygame.time.Clock() # création d'un objet horloge issu de Pygame permettant de gérer le temps et donc la vitesse du jeu
 
    ''' CREATION DU FOND '''
    
    
    fond = Entity() #Premièrement, le fond devient un objet de la Classe Entity, il fait partie des objets visibles du jeu
    
    fond.image = pygame.image.load('images_SUPERDINO2/interfaceniveau.png').convert() # on charge l'image de l'objet fond
    
    largeur_fond = fond.image.get_width()   # récupère la largeur de l'image du fond en pixels : 3740
    hauteur_fond = fond.image.get_height()  # récupère la hauteur de l'image du fond en pixels : 1100
    
    fond.rect = Rect(0,0, largeur_fond, hauteur_fond)
    # On attribue à notre objet fond ses caractéristiques rectangulaires
    # Son coin haut et gauche est 0,0, et il s'étend jusqu'à la largeur_fond et hauteur_fond
    

    ''' INITIALISATION DU PERSONNAGE '''
    
    
    joueur = Joueur(55, 55 )
    # joueur est une instance de la classe Joueur, une classe héritée de la classe Pygame Entity,
    # (55,55) sont les coordonnées de départ du joueur en pixels
    
    haut = gauche = droite = False
    #De base, le personnage de bouge pas


    ''' CREATION DE "ENSEMBLE": on rentre dans l'instance "ensemble" le fond et le joueur'''
    

    ensemble = pygame.sprite.Group()
    # On définit ensemble comme étant une instance de la classe pygame.sprite.Group()
    # Permet de regrouper, gérer et manipuler les multiples objets (ou instances) visibles
    
    # Ajout du fond dans l'instance ensemble (le fond est donc géré correctement par pygame, comme un sprite):
    ensemble.add(fond)

    # Ajout du joueur dans l'instance ensemble, on l'intègre ainsi aux objets pouvant être gérés par pygame
    ensemble.add(joueur) 
    

    ''' CREATION DU NIVEAU ET DES PLATEFORMES '''
    
    # On crée une liste NIVEAU qui contient tous les blocs de structure de la plateforme "codés" sous forme de caractères  
    NIVEAU = [                                                                      
        "3666666666666666661OOOOOOOOOO2666661OOOO2666666666666666666666666664",     
        "O                 1OOOOOOOOOO2     1OOOO2                          O",
        "O                 366OOOOOO664     1OOOO2                          O",
        "O                    366664        1OOOO2                          O",
        "O                                  1OOOO2                          O",
        "O            2                     1OOOO2                          O",
        "O           12               2     1OOOO2                          O",
        "15555552  1552    152    15552     1OOOO2                          O",
        "36666664  3664    1OO666666664     1OOOO2                         EO",
        "O6666664  3664    13664            1OOOO2                       152O",
        "O6666664  3664    13612            1OOOO2                       364O",
        "O6666664  3664    13612        3666666666664      1555555552       O",
        "O6666664  3664    13612                    12       OOOO           O",
        "O6666664  3664    13612                             OOOO           O",
        "O6666664  3664    13612                             OOOO           O",
        "O6666664  3664    136152  152    15552   155552     OOOO           O",
        "O6666664  3664    1361OO  OOO    15552   155552     OOOO           O",
        "O6666664MM3664MMMM1363OOMMOOOMM  36664MMM366664MMMMMOOOOMMMMMMMMMMMO",
        "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
        "1OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO2",]
    # En effet, chaque caractère (chiffre ou lettre) va correspondre à un graphisme (sprite) différent de 55*55 pixels

    plateformes = []
    # On crée une liste vide, plateformes, qui sera remplie progressivement par les objets sprites résultant des caractères contenus dans NIVEAU
    # Cette liste va regrouper tous les objets sprites qui rentrent en collision avec le joueur 


    x = y = 0 # On commence l'assimilation à x = 0 et y = 0, coordonnées de notre premier bloc de structure

    # Pour chaque caractère contenu dans la liste NIVEAU, on lui associe un sprite:     
    for ligne in NIVEAU:
        
        for lettre in ligne:
            
            if lettre == "O":
                
                p = Platform(x, y, 'images_SUPERDINO2/plateform.png')
                # On crée p comme instance de la classe Platform avec comme arguments les coordonnées x et y... 
                # ...ainsi que l'image du bloc correspondant au chiffre ou à la lettre correspondante (ici "0")
                # La classe Platform (qui est définie plus loin dans le code) va servir à charger notre image de bloc 
                # p devient ainsi un bloc rectangulaire texturé de coordonnées précises x et y
                
                # Ajout de p (le bloc texturé 55 x 55) dans la liste "plateformes" selon la méthode List append de Python :
                # les blocs s'ajoutent progressivement dans plateformes (les objets qui entrent en collision avec le joueur)
                plateformes.append(p)

                # Ajout de p à l'instance ensemble selon la méthode add de pygame.sprite.Group():
                # les blocs s'ajoutent progressivement dans ensemble (les objets visible du jeu)
                ensemble.add(p)

            # On répète la logique pour chaque caractère...
                
            if lettre == "1":
                
                p = Platform(x, y, 'images_SUPERDINO2/plateform1.png')  
                plateformes.append(p) 
                ensemble.add(p)

            if lettre == "2":

                p = Platform(x, y, 'images_SUPERDINO2/plateform2.png') 
                plateformes.append(p)
                ensemble.add(p)

            if lettre == "3":

                p = Platform(x, y, 'images_SUPERDINO2/plateform3.png')
                plateformes.append(p)
                ensemble.add(p)

            if lettre == "4":
                
                p = Platform(x, y, 'images_SUPERDINO2/plateform4.png') 
                plateformes.append(p)
                ensemble.add(p)
                
            if lettre == "5":
                
                p = Platform(x, y, 'images_SUPERDINO2/plateform5.png') 
                plateformes.append(p)
                ensemble.add(p)
                
            if lettre == "6":
                
                p = Platform(x, y, 'images_SUPERDINO2/plateform6.png')
                plateformes.append(p)
                ensemble.add(p)

            # On répète la même logique pour le bloc d'arrivée (celui de la victoire)...
            
            if lettre == "E":
                
                e = BlocVictoire(x, y)
                # e devient l'instance de la classe "BlocVictoire"
                # e représente le bloc texturé 55 x 55 de la victoire

                # Ajout de e à plateformes: les objets qui entrent en collision avec le joueur
                plateformes.append(e) 

                # Ajout de e à ensemble : les objets visible du jeu
                ensemble.add(e)
                
                

            #...Et les blocs de mort:
                
            if lettre == "M":
                
                m = BlocMort(x, y)
                plateformes.append(m) 
                ensemble.add(m)
                
            x += 55                 # x augmente de 55 pixels, car on avance d'un sprite vers la droite
            
        y += 55                 # y augmente de 55 pixels, car après avoir fait toute la ligne, on descend d'un sprite vers le bas... 
        x = 0                   # ...et on revient au début de la ligne

    
    ''' TRAITEMENT DE LA CAMERA '''

    # Determination du nombre total de pixel dans la première ligne du niveau
    # Autrement dit, sa largeur totale en pixels
    # Pour cela, on prend chaque élément de la première ligne de la liste "niveau", et on la multiplie par le nb de pixel dans un sprite (55)
    largeur_niveau_total = len(NIVEAU[0])*55

    # Determination de la hauteur totale en pixels
    # Pour cela, on détermine le nombre d'éléments dans la liste niveau, que l'on multiplie par 55
    hauteur_niveau_total = len(NIVEAU)*55

    # Création de l'instance "camera" issue de la classe "Camera"
    # camera correspondra à un rectangle de la dimension du niveau
    camera = Camera(largeur_niveau_total, hauteur_niveau_total) 
    
    
    '''

    COMMANDES D'ACTIONS - BOUCLE PRINCIPALE DU JEU
        
    '''

    # Après avoir préparé tout ce dont on avait besoin, le jeu commence à tourner ici.

    while 1:
        
        # Définition du nombre d'images par seconde (et de la vitesse du jeu)
        horloge.tick(65)

        # Traitement des événements gérés par Pygame

        for e in pygame.event.get():

            # Si on appuie sur la croix en haut à droite de la fenètre d'affichage, ou
            # Si on appuie sur echap
            # Le jeu se ferme
            
            if e.type == QUIT:
                pygame.quit()
                exit()
                    
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                pygame.quit()
                exit()

            # Gestion des variables de mouvement du joueur (haut, gauche, droit) en fonction de la touche appuyée
                             
            if e.type == KEYDOWN and e.key == K_UP:
                haut = True
                             
            if e.type == KEYDOWN and e.key == K_LEFT:
                gauche = True
                
            if e.type == KEYDOWN and e.key == K_RIGHT:
                droite = True

            # Gestion des variables de mouvement du joueur en fonction des touches relevées (non-appuyées)
            # NOTE: dans ce cas-là, les mouvements sont arrêtés
                
            if e.type == KEYUP and e.key == K_UP:
                haut = False
                
            if e.type == KEYUP and e.key == K_RIGHT:
                droite = False
                
            if e.type == KEYUP and e.key == K_LEFT:
                gauche = False
        
        # Application des mouvements au joueur en fonction des variables de mouvement et des blocs de structure:
        # execution de la méthode mouvements de la classe Joueur avec les arguments : haut, gauche, droite, plateformes = liste des blocs avec lesquels le joueur entre en collision
        joueur.mouvements(haut, gauche, droite, plateformes)

        # Actualisation de la caméra en fonction du déplacement du joueur
        # Elle suit le sprite du joueur par application de la méthode mouvements de la classe Camera
        camera.mouvements(joueur)
        
        ### BOUCLE D'AFFICHAGE ###
        
        # Pour tout élément de "ensemble" (l'ensemble des objets visibles)
        # Pygame affiche cet élément qui est déplacé selon la méthode appliquer de la classe Camera 
        # Ainsi, la zone affichée correspond à la fenêtre entourant le joueur
        for e in ensemble:
            fenetre.blit(e.image, camera.appliquer(e))

        # Raffraichissement de l'écran par pygame
        pygame.display.update()

        
        ''' FIN DE LA BOUCLE PRINCIPALE DU JEU '''




'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

DEFINITION DES CLASSES ET METHODES (OU FONCTIONS DE CLASSES)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Notre foncton "main()" fait en permanance appel à des classes que nous expliquons maintenant.


''' LA CLASSE JOUEUR '''
# La Classe Joueur permet de créer et gérer le joueur, ses mouvements et ses collisions avec les plateformes (ou blocs de structure)
# Elle hérite de la classe Entity, ce qui lui permet de créer le sprite visible du joueur

class Joueur(Entity):

    # fonction d'initialisation de tous les attributs du joueur
    def __init__(self, x, y):

        # Initialisation de la classe Entity()
        Entity.__init__(self)

        # MOUVEMENT DU JOUEUR:
        # Au départ, il est immobile...
        self.xvel = 0
        self.yvel = 0

        # ...et n'est pas sur le sol, il tombe donc.
        self.onGround = False

        # Chargement de l'image du joueur placée dans le dossier "images"
        # convert_alpha permet de conserver la transparence du fond de l'image du joueur
        self.image = pygame.image.load('images_SUPERDINO2/base_droite.png').convert_alpha()

        # Redimensionnement de l'image du joueur
        # Sa taille revient à taille_perso x taille_perso (65 x 65)
        self.image = pygame.transform.scale(self.image, (taille_perso, taille_perso))

        # Caractérisation du joueur en tant que rectangle de cotés taille_perso
        # Celui-ci stock les coordonnées du joueur ainsi que sa taille   
        self.rect = pygame.rect.Rect(x, y, taille_perso, taille_perso)

    # méthode permettant de gérer les mouvements du joueur    
    def mouvements(self, haut, gauche, droite, plateformes):

        '''LES DIFFERENTS SONS'''

        # chargement des sons
        sonjump = pygame.mixer.Sound("sons/Jump.wav")
        # on definit le volume
        sonjump.set_volume(0.3)   # HP à 30%

        # S'il saute, il y a 2 possibilités:
        if haut:

            # S'il est sur le sol, il monte de 10 pixels en 10 pixels
            if self.onGround:
                self.yvel -= 10
                sonjump.play()
            
            # S'il est dans les airs, il ne peut pas sauter
            if not self.onGround:
                pass
            
        # Si l'utilisateur a appuyé sur la touche gauche :       
        if gauche:
            self.xvel = -8
        # il va vers la gauche de 8 pixels en 8 pixels

        # Si l'utilisateur a appuyé sur la touche droite :       
        if droite:
            self.xvel = 8
        # il va vers la droite de 8 pixels en 8 pixels

        # La gravité:
        if not self.onGround:
            self.yvel += 0.3
        
        if not(gauche or droite):
            self.xvel = 0
            
        # Incrémentation sur l'axe des x
        self.rect.right += self.xvel
        
        # Application de la méthode collision sur l'axe des x
        # détecte la collision et empêche le joueur de traverser le bloc avec lequel il entre en collision
        self.collision(self.xvel, 0, plateformes)
        
        # Incrémentation sur l'axe des y
        self.rect.top += self.yvel
        
        # On part du principe que le joueur est dans les airs
        self.onGround = False;
        
        # Application de la méthode collision sur l'axe des y
        # détecte la collision et empêche le joueur de traverser le bloc avec lequel il entre en collision
        self.collision(0, self.yvel, plateformes)


    # Cette fonction permet une détection de la collision du joueur avec les objets de structure du niveau (regroupés dans platfomes)
    # Elle agit en conséquence : bloque le mouvement, charge la victoire ou charge la mort...
    def collision(self, xvel, yvel, plateformes):

        #Appel du son dans le fichier son
        son_gameover = pygame.mixer.Sound("sons/Gameover.wav")
        son_gameover.set_volume(0.5)   # HP à 50%

        son_victoire = pygame.mixer.Sound("sons/New.wav")
        son_victoire.set_volume(0.5)
        
        # Pour chaque bloc du niveau
        for p in plateformes:
            
            if pygame.sprite.collide_rect(self, p):
            # Appel d'une fonction de détection de collision de rectangles : pygame.sprite.collide_rect(self, p)
            # Pygame détecte la collision entre le rectangle du joueur (self) et l'objet p du niveau
            # Donc, en cas de collision :
            
                x = y = 0
                
                # Si p est une instance de la classe BlocVictoire (bloc d'arrivée)
                # Autrement dit, si p correspond au bloc d'arrivée
                if isinstance(p, BlocVictoire):

                    # Chargement de l'écran de la victoire et affichage de cet écran, avec une petite musique
                    son_victoire.play()
                    ecran_reussite = pygame.image.load('images_SUPERDINO2/BRAVO.png').convert()
                    fenetre.blit(ecran_reussite, (0,0))
                    pygame.display.update()

                    #Attente de 3000 ms (pour pouvoir voir l'image)
                    pygame.time.wait(3000)

                    #Le jeu se ferme
                    exit()

                # Même principe avec le BlocMort:
                if isinstance(p, BlocMort):

                    son_gameover.play()
                    ecran_mort = pygame.image.load('images_SUPERDINO2/GAME_OVER.png').convert()
                    fenetre.blit(ecran_mort, (0,0))
                    pygame.display.update()
                    
                    pygame.time.wait(3000)

                    # Seulement ici, après avoir vu l'image de défaite, on relance le jeu
                    main()

                
                # EMPECHE LE JOUEUR DE TRAVERSER LE BLOC S'IL Y A COLLISION
                
                if xvel > 0:                        
                    self.rect.right = p.rect.left
                # Si le joueur entre en collision quand il va sur la droite (donc lorsque xvel > 0)
                # Son coté droit (rectangle) est égale au coté gauche de l'objet (rectangle) avec lequel il entre en collision
                # Il ne peut donc plus avancer
                    
                if xvel < 0:
                    self.rect.left = p.rect.right
                # Si le joueur entre en collision quand il va sur la gauche
                # Son coté gauche (rectangle) est égale au coté droit de l'objet (rectangle) avec lequel il entre en collision
                    
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                # Si le joueur entre en collision lorsqu'il tombe
                # Son coté bas est égale au coté haut de l'objet avec lequel il entre en collision
                # Il est sur le sol, donc self.onGround = True
                    
                if yvel < 0:
                    self.rect.top = p.rect.bottom
                # Si le joueur entre en collision lorsqu'il saute
                # Son coté haut est égale au coté bas de l'objet avec lequel il entre en collision


''' LA CLASSE PLATEFORME '''
# La Classe Platform correspond aux blocs de structure du jeu ne pouvant pas être traversés par le joueur (= aux murs)

class Platform(Entity):
    
    def __init__(self, x, y, bloc_structure):

        #Initialisation de l'Entity
        Entity.__init__(self)

        #Chargement de l'image de chaque plateforme en fonction du "bloc-structure" choisi
        #Le "bloc_structure" représente un argument qui est défini dans main() lors de la construction de la liste "plateformes"
        self.image = pygame.image.load(bloc_structure).convert()

        # Redimensionnement à 55 x 55 pixels
        self.image = pygame.transform.scale(self.image, (55, 55))

        # Caractérisation du bloc comme un rectangle de 55*55 de côtés
        self.rect = Rect(x, y, 55, 55)


''' LES CLASSES BLOCVICTOIRE ET BLOCMORT '''
# La Classe BlocVictoire correspond au bloc de sortie, la zone que le joueur cherche à atteindre pour gagner
# La Classe BlocMort correspond aux zones du jeu entrainant la mort du joueur
# Nous les avons différenciées du reste des objets visibles du jeu pour plus de clarté et afin de les détecter plus simplement
# La logique pour ces 2 classes est la même que celle d'Entity. Elle héritent toutes deux d'Entity.

class BlocVictoire(Entity):
    
    def __init__(self, x, y):
        
        Entity.__init__(self)

        # Création d'un bloc de surface 55 x 55
        self.image = Surface((55, 55))
        
        # Coloration du bloc en bleu
        self.image.fill(Color("#0000FF"))

        # Caractérisation en tant que rectangle de 55 x 55 et de coordonnées (x, y)
        self.rect = Rect(x, y, 55, 55)

# (La logique est identique)
class BlocMort(Entity):
    
    def __init__(self, x, y):
        
        Entity.__init__(self)
        
        self.image = Surface((55, 55))
       
        # Coloration du bloc en rouge
        self.image.fill(Color("#FF0000"))
        
        self.rect = Rect(x, y, 55, 55)



''' CLASSE CAMERA '''
# La Classe Camera coorespond à la zone affichée du jeu, ce qui est visible et affiché


class Camera():

    def __init__(self, largeur, hauteur):
        
        self.rectangle_caméra = Rect(0, 0, largeur, hauteur)
        # Création du rectangle de la caméra
        # Son coin supérieur gauche de coordonnées (0,0) s'étend selon les valeurs de largeur et hauteur
    

    def mouvements(self, cible): # methode qui recalcule la position la caméra pour qu'elle soit centrée par raport à la cible (au joueur)
        
        x, y, _, _ = cible.rect     #_ = ignorer
        _, _, largeur, hauteur = self.rectangle_caméra
        x, y, _, _ = x - DemiLargeur, y - DemiHauteur, largeur, hauteur # place la caméra pour que la cible soit en son milieu

        # LIMITES DES DEPLACEMENTS DE LA CAMERA (son cadre)
        # Il ne faut pas qu'elle sorte des limites du niveau
        
        if x < 0: x = 0                                         # la caméra ne peut pas aller plus loin que l'extrème gauche du niveau
        
        if x > self.rectangle_caméra.width - LargeurInterface : # self.rectangle_caméra.width correspond à la largeur totale du niveau
            x = self.rectangle_caméra.width - LargeurInterface  # la caméra ne peut pas aller plus loin que l'extrème droite du niveau
            
        if y < 0 : y = 0                                        # la caméra ne peut pas aller plus haut que l'extrème haut du niveau
        
        if y > self.rectangle_caméra.height - HauteurInterface :# self.rectangle_caméra.height correspond à la hauteur totale du niveau
            y = self.rectangle_caméra.height - HauteurInterface # la caméra ne peut pas aller plus loin que l'extrème bas du niveau
            
        self.rectangle_caméra = Rect(-x, -y , largeur, hauteur) # Les coordonnées initiales du rectangle de la camera deviennent (-x, -y)
                                                                # ces coordonnées (-x, -y) représentent le décalage qui sera appliqué aux 
                                                                # sprites de la zone de la caméra afin qu'ils soient affichés dans la fenêtre
                                                                
    # méthode qui exécute le décalage (déplacement) des sprites de la caméra dans la zone qui sera affichée par fenetre.blit()
    def appliquer(self, sprite):
        return sprite.rect.move(self.rectangle_caméra.topleft)
        
        
''' FIN DES CLASSES ET FONCTIONS '''




# Lancement du jeu par la fonction "main()"
# Nous permet d'exécuter le Moteur de facon indépendante, sans recourir au Code Principal
# Afin de pouvoir tester plus facilement le code
if __name__ == "__main__": main()

