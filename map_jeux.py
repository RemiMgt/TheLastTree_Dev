import pygame

class Map(pygame.sprite.Sprite) :
    def __init__(self) :
        super().__init__()
        self.image = pygame.image.load("assets/map.png")
        self.rect = self.image.get_rect()
        self.rect.x = -1050
        self.rect.y = -700