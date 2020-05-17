import pygame

class Player(pygame.sprite.Sprite) :
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

    def __init__(self, game) :
        super().__init__()
        self.image = pygame.image.load("sprite/rien_bas.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.game = game
        self.rect.x = 740
        self.rect.y = 380
        self.vitesse = 20
        self.direction = "B"

    def move_haut(self) :
        self.direction = "H"
        self.image = pygame.image.load("sprite/cour_haut1.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.game.map.rect.y = self.game.map.rect.y + self.vitesse

    def move_bas(self) :
        self.direction = "B"
        self.image = pygame.image.load("sprite/cour_bas1.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.game.map.rect.y = self.game.map.rect.y - self.vitesse

    def move_droite(self) :
        self.direction = "D"
        self.image = pygame.image.load("sprite/cour_droite1.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.game.map.rect.x = self.game.map.rect.x - self.vitesse

    def move_gauche(self) :
        self.direction = "G"
        self.image = pygame.image.load("sprite/cour_gauche1.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.game.map.rect.x = self.game.map.rect.x + self.vitesse