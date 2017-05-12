import pygame
from pygame import *

LargeurInterface = 640
HauteurInterface = 480
DemiLargeur = int(LargeurInterface / 2)
DemiHauteur = int(HauteurInterface / 2)

taille_perso = 55
screen = pygame.display.set_mode((LargeurInterface, HauteurInterface))


# section principale du jeu : le module main()     
def main():
    pygame.init()
    pygame.display.set_caption("Super Dino") 

    timer = pygame.time.Clock()

    up = down = left = right = running = False
    
    bg = Entity() # bg est une instance de la Classe Entity, elle fait partie des objets visibles du jeu, il s'agit du fond (background),  
    
    bg.image = pygame.image.load('images/interfaceniveau.png').convert() # on charge l'image du fond dans bg 
    width = bg.image.get_width()    # récupère la largeur de l'image du fond en pixels ; 3740
    height = bg.image.get_height()  # récupère la hauteur de l'image du fond en pixels ; 1100
    bg.rect = Rect(0,0, width, height) # indique à pygame que bg est un rectangle dont le coin haut et gauche est 0,0 et de largeur width et de hauteur height
    
    entities = pygame.sprite.Group() #définit entities comme étant un groupe de sprites (instance de la classe pygame sprite group qui permet de gérer de multiples objets Sprite)
    entities.add(bg) # ajoute le rectangle de l'image de fond dans entities (le fond est visible) 

    player = Player(55, 55 ) # player est une instance de Player (le joueur), une classe qui hérite de la classe Pygame Entity, (55,55) sont les coordonnées de départ du joueur en pixels
    platforms = []

    x = y = 0
    
    level = [                                                                       # on construit le niveau avec les blocs de structure que le joueur ne peut traverser
        "3OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO4",     # chaque chiffre correspond à un graphisme (sprite) différent de 55*55 pixels
        "O                 1OOOOOOOOOO2     1OOOO2                          O",
        "O                 366OOOOOO664     1OOOO2                          O",
        "O                    366664        1OOOO2                          O",
        "O                                  1OOOO2                          O",
        "O            2                     1OOOO2                          O",
        "O           12               2     1OOOO2                          O",
        "15555552  1552    152    15552     1OOOO2                          O",
        "36666664  3664    1OO666666664     1OOOO2                         EO",
        "O                  3664            1OOOO2                       152O",
        "O                    12            1OOOO2                       364O",
        "O                    12        3666666666664      1555555552       O",
        "O                    12                    12       OOOO           O",
        "O                    12                             OOOO           O",
        "O                    12                             OOOO           O",
        "O                    152  152    15552   155552     OOOO           O",
        "O                    1OO  OOO    15552   155552     OOOO           O",
        "OMMMMMMMMMMMMMMMMMMMM3OOMMOOOMM  36664MMM366664MMMMMOOOOMMMMMMMMMMMO",
        "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
        "1OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO2",]
    
    # constrction du niveau
    for ligne in level:
        for lettre in ligne:     # pour chaque caractère correspondant à un graphisme (sprite) différent de 55*55 pixels
            if lettre == "O":
                p = Platform(x, y, 'images/plateform.png') # on charge un sprite de type "0", de coordonées x,y  
                platforms.append(p) # on ajoute ce sprite de structure à l'instance platforms ; #append = mettre l'élément entre parenthèse à la fin de la liste en constitution
                entities.add(p)     # on ajoute ce sprite de structure à l'instance entities, les objets visibles du jeu
            if lettre == "1":
                p = Platform(x, y, 'images/plateform1.png') # on charge un sprite de type "1", de coordonées x,y  
                platforms.append(p) # on ajoute ce sprite de structure à l'instance platforms 
                entities.add(p)     # on ajoute ce sprite de structure à l'instance entities, les objets visibles du jeu
            if lettre == "2":
                p = Platform(x, y, 'images/plateform2.png') # on charge un sprite de type "2", de coordonées x,y  
                platforms.append(p)
                entities.add(p)
            if lettre == "3":
                p = Platform(x, y, 'images/plateform3.png') # on charge un sprite de type "3", de coordonées x,y  
                platforms.append(p)
                entities.add(p)
            if lettre == "4":
                p = Platform(x, y, 'images/plateform4.png') # on charge un sprite de type "4", de coordonées x,y  
                platforms.append(p)
                entities.add(p)
            if lettre == "5":
                p = Platform(x, y, 'images/plateform5.png') # on charge un sprite de type "5", de coordonées x,y  
                platforms.append(p)
                entities.add(p)
            if lettre == "6":
                p = Platform(x, y, 'images/plateform6.png') # on charge un sprite de type "6", de coordonées x,y  
                platforms.append(p)
                entities.add(p)                 
            if lettre == "E":
                e = ExitBlock(x, y, 'images/arrivee.png')   # on charge un sprite de type "E" = exit, de coordonées x,y, dans l'instance e de ExitBlock, classe héritée de la classe Platform
                platforms.append(e) # on ajoute ce sprite de structure à l'instance platforms 
                entities.add(e)     # on ajoute ce sprite de structure à l'instance entities, les objets visibles du jeu, car la sortie (exit) en fait partie
            if lettre == "M":
                m = BlockMort(x, y) # on charge un sprite de type "M" = mort, de coordonées x,y, dans l'instance m de BlockMort, classe héritée de la classe Entity
                platforms.append(m) # on ajoute ce sprite de structure à l'instance platforms 
                entities.add(m)     # on ajoute ce sprite de structure à l'instance entities, les objets visibles du jeu, car les blocs entrainant la mort en font partie 
            x += 55                 # on incrémente x de 55 pixels par caractère = sprite
        y += 55                     # on incrémente y de 55 pixels par caractère = sprite
        x = 0                       # passage à la ligne suivante

    entities.add(player)            # on ajoute le joueur à l'instance entities, on l'intègre ainsi aux objets visibles
    
#Bases pour la caméra:

    total_level_width  = len(level[0])*55   #nb de pixels horizontales du niveau défini par le nombre de caractères de 55*55 pixels de la première ligne
    total_level_height = len(level)*55      #nb de pixels horizontales du niveau défini par le nombre de lignes *55 pixels
    
    camera = Camera(total_level_width, total_level_height) # camera est une instance de la classe Camera, elle correspond à un rectangle de dimension du niveau 
    

# Les commandes d'action, boucle principale du jeu
    while 1:
        timer.tick(60)

        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                exit()
                    
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                pygame.quit()
                exit()
                             
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                down = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYDOWN and e.key == K_SPACE:
                running = True
            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_DOWN:
                down = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
 
        camera.update(player) # La caméra s'actualise en fonction du déplacement du joueur, elle suit le joueur par application de la methode update de la classe Camera  
                              # sur le sprite rectangulaire du joueur de 55*55 pixels de coordonnées x,y (le joueur est centré sauf si la camera est aux extremités du niveau)
                              
        # on attribue au joueur son mouvement
        player.update(up, down, left, right, running, platforms)
        
        for e in entities:
            screen.blit(e.image, camera.appliquer(e)) # affiche les sprites de entities (les objets visibles du jeu) limités (= appliqués) à la zone caméra autour du personnage
        pygame.display.update()
# fin de la boucle principale du jeu

# ************************************************************************
# ************ définition des classes et méthodes ************************ 
# ************************************************************************

# La Classe Entity regroupe tous les objets visibles du jeu
class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #crée la classe Entity qui hérite de la Classe pygame.sprite.Sprite, Classe de base de Pygame qui regroupe tous les objets visibles du jeu

# La Classe Player correspond au joueur, ses mouvements et ses collisions avec la plateforme
class Player(Entity): # Player, objet qui représente le joueur, est une classe qui hérite de la classe Entity (le joueur fait partie des objets visibles du jeu)
    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = 0 # au départ le jeueur est immobile...
        self.yvel = 0
        self.onGround = False  # ...et n'est pas sur le sol, il va donc tomber
        self.image = pygame.image.load('images/base_droite.png').convert_alpha() # le jeueur est représenté par l'image base_droit.png placée dans le dossier images
        self.image = pygame.transform.scale(self.image, (taille_perso, taille_perso)) # la taille de l'image du jeueur est adaptée à taille_perso
        self.rect = pygame.rect.Rect(x, y, taille_perso, taille_perso)  # le joueur est défini comme un objet de Pygame (Rect) qui stock les coordonnées du joueur comme un rectangle   
                                                                        # de cotés taille_perso (x, y, largeur, hauteur) 
    def update(self, up, down, left, right, running, platforms): # définit la fonction update du joueur (methode de Player), sa mise à jour = son mouvement
        if up:
            if self.onGround: # le joueur ne peut sauter que s'il est sur le sol
                self.yvel -= 10
        if down:
            pass
        if running: 
            pass
            
        if left:
            self.xvel = -8
        if right:
            self.xvel = 8
        if not self.onGround:
            # only accelerate with gravity if in the air
            self.yvel += 0.3
            # max falling speed
            if self.yvel > 100:
                self.yvel = 100
        if not(left or right):
            self.xvel = 0
        # increment in x direction
        self.rect.left += self.xvel
        # do x-axis collisions
        self.collide(self.xvel, 0, platforms)
        # increment in y direction
        self.rect.top += self.yvel
        # assuming we're in the air
        self.onGround = False;
        # do y-axis collisions
        self.collide(0, self.yvel, platforms)

    def collide(self, xvel, yvel, platforms): # définit la fonction collide (methode de Player), détection de la collision du joueur avec des objets de structure du level (regroupés dans platfomrs) que le joueur ne peut pas traverser)
        for p in platforms:
            if pygame.sprite.collide_rect(self, p): # fonction de détection de collision de rectangles de Pygame = du joueur avec les objets (blocs de structure) du level, donc si collision
                if isinstance(p, ExitBlock):    # si p (le joueur) est une instance d'ExitBlock (l'arrivée) = il entre en collision avec le bloc d'arrivée, alors...
                    ecran_reussite = pygame.image.load('images/BRAVO.png').convert() #...on charge l'écran de la victoire puis le programme se termine 
                    screen.blit(ecran_reussite, (0,0))
                    pygame.display.update()
                    pygame.time.wait(3000)      # attente de 3000 millisecondes
                    exit()                      # fin
                    
                if isinstance(p, BlockMort):    # si p (le joueur) est une instance de BlockMort (la mort) = il entre en collision avec un bloc de mort, alors...
                    ecran_mort = pygame.image.load('images/GAME_OVER.png').convert() #...on charge l'écran de la défaite puis le programme recommence 
                    screen.blit(ecran_mort, (0,0))
                    pygame.display.update()     # rafraichissement de l'écran
                    pygame.time.wait(3000)      # attente de 3000 millisecondes
                    main()                      # retour au début du jeu

                if xvel > 0:                        
                    self.rect.right = p.rect.left   # si le joueur entre en collision quand il va sur la droite, son coté droit (rectangle) est égale au coté gauche de l'objet (rectangle) avec lequel il entre en collision  
                    
                if xvel < 0:
                    self.rect.left = p.rect.right   # si le joueur entre en collision quand il va sur la gauche, son coté gauche (rectangle) est égale au coté droit de l'objet (rectangle) avec lequel il entre en collision
                    
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                    
                if yvel < 0:
                    self.rect.top = p.rect.bottom

# La Classe Platform correspond aux blocs de structure du jeu ne pouvant pas être traversés par le joueur (= aux murs)
class Platform(Entity):
    def __init__(self, x, y, bloc_structure):
        Entity.__init__(self)
        self.image = pygame.image.load(bloc_structure).convert()
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = Rect(x, y, 55, 55)

# La Classe ExitBlock correspond au bloc de sortie, la zone que dit atteindre le joueur pour gagner
class ExitBlock(Platform):
    def __init__(self, x, y, bloc_structure):
        Platform.__init__(self, x, y, bloc_structure)
        self.image.convert_alpha() #meilleure gestion des images.png avec fond transparent

# La Classe BlockMort correspond aux zones du jeu entrainant la mort du joueur...
class BlockMort(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = Surface((55, 55))
        self.image.convert()
        self.image.fill(Color("#FF0000"))
        self.rect = Rect(x, y, 55, 55)

# La Classe Camera coorespond à la zone affichée du jeu, ce qui est visible et affiché
class Camera():

    def __init__(self, largeur, hauteur): #initialisation de toutes les variables de la caméra -------------------  
        self.rectangle_caméra = Rect(0, 0, largeur, hauteur) #Le Rect permet de créer un rectangle de coin supérieur gauche de coordonnées (0,0) qui va s'étendre selon les valeurs de largeur et hauteur
    
    def appliquer(self, cible): # methode qui déplace le rectangle de la camera (centrée sur la cible) vers le coin haut et gauche (qui sera ainsi affiché par screen.blit)
        return cible.rect.move(self.rectangle_caméra.topleft)   # déplacement de (-x, -y) conformément à la méthode update (self, cible)

    def update(self, cible): # methode qui recalcule la position la caméra pour qu'elle soit centrée par raport à la cible
        x, y, _, _ = cible.rect     #_ = ignorer
        _, _, largeur, hauteur = self.rectangle_caméra
        x, y, _, _ = x - DemiLargeur, y - DemiHauteur, largeur, hauteur # place la caméra pour que la cible soit en son milieu 
        # impose les limites de déplacement de la camera afin qu'elle ne sorte pas des limites du niveau (level)
        if x < 0: x = 0                                         # la caméra ne peut pas aller plus loin que l'extrème gauche du niveau
        if x > self.rectangle_caméra.width - LargeurInterface : # self.rectangle_caméra.width correspond à la largeur totale du niveau
            x = self.rectangle_caméra.width - LargeurInterface  # la caméra ne peut pas aller plus loin que l'extrème droite du niveau
        if y < 0 : y = 0                                        # la caméra ne peut pas aller plus haut que l'extrème haut du niveau
        if y > self.rectangle_caméra.height - HauteurInterface :# self.rectangle_caméra.height correspond à la hauteur totale du niveau
            y = self.rectangle_caméra.height - HauteurInterface # la caméra ne peut pas aller plus loin que l'extrème bas du niveau
        self.rectangle_caméra = Rect(-x, -y , largeur, hauteur) # Les coordonnées initiales du rectangle de la camera deviennent (-x, -y)
        


if __name__ == "__main__":      # permet à moteur d'être exécuté de facon indépendante, sans la partie début
   main()

