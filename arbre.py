import pygame

class Arbre(pygame.sprite.Sprite) :
    def __init__(self, game) :
        super().__init__()
        self.image = pygame.image.load("assets/arbre.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.game = game
        self.rect.x = self.game.map.rect.x + 1500
        self.rect.y = self.game.map.rect.y + 1500