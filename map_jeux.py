import pygame

class Map(pygame.sprite.Sprite) :
    def __init__(self) :
        super().__init__()
        self.image = pygame.image.load("assets/map.png")
        self.image = pygame.transform.scale(self.image, (3000, 3000))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0