import pygame
from random import *

class Bucheron_H(pygame.sprite.Sprite) :
    def __init__(self, game) :
        super().__init__()
        self.image = pygame.image.load("assets/bucheron.png")
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.game = game
        self.rect.y = randint(game.map.rect.y, game.map.rect.y + 3000)
        self.vitesse = 10

    def move(self) :
        if self.rect.x < self.game.arbre.rect.x :
            self.rect.x = self.rect.x + self.vitesse
        if self.rect.x > self.game.arbre.rect.x :
            self.rect.x = self.rect.x - self.vitesse
        if self.rect.y > self.game.arbre.rect.y :
            self.rect.y = self.rect.y - self.vitesse
        if self.rect.y < self.game.arbre.rect.y :
            self.rect.y = self.rect.y + self.vitesse