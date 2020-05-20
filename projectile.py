import pygame

class Projectile(pygame.sprite.Sprite) :
    def __init__(self, game, direction) :
        super().__init__()
        self.image = pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.game = game
        self.rect.x = game.player.rect.x + 20
        self.rect.y = game.player.rect.y + 30
        self.vitesse = 15
        self.direction = direction

    def move(self) :
        if self.direction == "H" :
            self.rect.y = self.rect.y - self.vitesse
        elif self.direction == "B" :
            self.rect.y = self.rect.y + self.vitesse
        elif self.direction == "D" :
            self.rect.x = self.rect.x + self.vitesse
        elif self.direction == "G" :
            self.rect.x = self.rect.x - self.vitesse
        #Diagonale