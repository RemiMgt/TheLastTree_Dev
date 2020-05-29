import pygame

class Player(pygame.sprite.Sprite) :
    '''
    RIEN_BAS = pygame.image.load("sprite/rien_bas.png")
    COUR_DROITE1 = pygame.image.load("sprite/cour_droite1.png")
    COUR_DROITE2 = pygame.image.load("sprite/cour_droite2.png")
    COUR_GAUCHE1 = pygame.image.load("sprite/cour_gauche1.png")
    COUR_GAUCHE2 = pygame.image.load("sprite/cour_gauche2.png")
    COUR_BAS1 = pygame.image.load("sprite/cour_bas1.png")
    COUR_HAUT1 = pygame.image.load("sprite/cour_haut1.png")
    RIEN_DROITE = pygame.image.load("sprite/rien_droite.png")
    RIEN_GAUCHE = pygame.image.load("sprite/rien_gauche.png")
    RIEN_HAUT = pygame.image.load("sprite/rien_haut.png")
    '''

    def __init__(self, game) :
        super().__init__()
        self.index_haut = 0
        self.index_bas = 0
        self.index_droite = 0
        self.index_gauche = 0
        self.tab_haut = []
        self.tab_haut.append(pygame.image.load("sprite/rien_haut.png"))
        self.tab_haut.append(pygame.image.load("sprite/cour_haut1.png"))
        self.tab_bas = []
        self.tab_bas.append(pygame.image.load("sprite/rien_bas.png"))
        self.tab_bas.append(pygame.image.load("sprite/cour_bas1.png"))
        self.tab_droite = []
        self.tab_droite.append(pygame.image.load("sprite/cour_droite1.png"))
        self.tab_droite.append(pygame.image.load("sprite/cour_droite2.png"))
        self.tab_gauche = []
        self.tab_gauche.append(pygame.image.load("sprite/cour_gauche1.png"))
        self.tab_gauche.append(pygame.image.load("sprite/cour_gauche2.png"))
        self.image = self.tab_bas[self.index_bas]
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect()
        self.game = game
        self.rect.x = 740
        self.rect.y = 380
        self.vitesse = 30
        self.vitesse_joy = 15
        self.direction = "B"

    def move_haut(self) :
        self.direction = "H"
        self.image = pygame.image.load("sprite/cour_haut1.png")
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.game.map.rect.y = self.game.map.rect.y + self.vitesse

    def move_bas(self) :
        self.direction = "B"
        self.image = pygame.image.load("sprite/cour_bas1.png")
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.game.map.rect.y = self.game.map.rect.y - self.vitesse

    def move_droite(self) :
        self.direction = "D"
        self.image = pygame.image.load("sprite/cour_droite1.png")
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.game.map.rect.x = self.game.map.rect.x - self.vitesse

    def move_gauche(self) :
        self.direction = "G"
        self.image = pygame.image.load("sprite/cour_gauche1.png")
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.game.map.rect.x = self.game.map.rect.x + self.vitesse



    def move_haut_joy(self, game) :
        self.direction = "H"
        self.image = pygame.image.load("sprite/cour_haut1.png")
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.game.map.rect.y = self.game.map.rect.y + self.vitesse_joy

    def move_bas_joy(self) :
        self.direction = "B"
        self.image = pygame.image.load("sprite/cour_bas1.png")
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.game.map.rect.y = self.game.map.rect.y - self.vitesse_joy

    def move_droite_joy(self) :
        self.direction = "D"
        self.image = pygame.image.load("sprite/cour_droite1.png")
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.game.map.rect.x = self.game.map.rect.x - self.vitesse_joy

    def move_gauche_joy(self) :
        self.direction = "G"
        self.image = pygame.image.load("sprite/cour_gauche1.png")
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.game.map.rect.x = self.game.map.rect.x + self.vitesse_joy



    def animation_haut(self):
        self.index_haut += 1

        if self.index_haut >= len(self.tab_haut):
            self.index_haut = 0

        self.image = self.tab_haut[self.index_haut]
        self.image = pygame.transform.scale(self.image, (120, 120))

    def animation_bas(self):
        self.index_bas += 1

        if self.index_bas >= len(self.tab_bas):
            self.index_bas = 0

        self.image = self.tab_bas[self.index_bas]
        self.image = pygame.transform.scale(self.image, (120, 120))

    def animation_droite(self):
        self.index_droite += 1

        if self.index_droite >= len(self.tab_droite):
            self.index_droite = 0

        self.image = self.tab_droite[self.index_droite]
        self.image = pygame.transform.scale(self.image, (120, 120))

    def animation_gauche(self):
        self.index_gauche += 1

        if self.index_gauche >= len(self.tab_gauche):
            self.index_gauche = 0

        self.image = self.tab_gauche[self.index_gauche]
        self.image = pygame.transform.scale(self.image, (120, 120))