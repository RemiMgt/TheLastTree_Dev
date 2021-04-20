import pygame
from random import *

def move_player_H(self) : 
        if self.game.player.direction == "D" :
            self.rect.x = self.rect.x - self.vitesse / 2
        if self.game.player.direction == "G" :
            self.rect.x = self.rect.x + self.vitesse / 2
        if self.game.player.direction == "H" :
            self.rect.y = self.rect.y + self.vitesse / 2
        if self.game.player.direction == "B" :
            self.rect.y = self.rect.y - self.vitesse / 2

class Bucheron_H(pygame.sprite.Sprite) :
    def __init__(self, game) :
        super().__init__()
        self.image = pygame.image.load("assets/bucheron.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.game = game
        self.rect.y = randint(game.map.rect.y, game.map.rect.y + 3000)
        self.vitesse = 8

    def move(self) :
        if self.rect.x < self.game.arbre.rect.x :
            if not self.rect.colliderect(self.game.arbre.rect) :
                move_player_H(self)
                self.rect.x = self.rect.x + self.vitesse
            else :
                self.game.active_musique = True
                self.game.GAME_OVER = True
                self.game.all_bucheron_C.empty()
                self.game.all_bucheron_H.empty()
                self.game.all_projectile.empty()
        if self.rect.x > self.game.arbre.rect.x :
            if not self.rect.colliderect(self.game.arbre.rect) :
                move_player_H(self)
                self.rect.x = self.rect.x - self.vitesse
            else :
                self.game.active_musique = True
                self.game.GAME_OVER = True
                self.game.all_bucheron_C.empty()
                self.game.all_bucheron_H.empty()
                self.game.all_projectile.empty()
        if self.rect.y > self.game.arbre.rect.y :
            if not self.rect.colliderect(self.game.arbre.rect) :
                move_player_H(self)
                self.rect.y = self.rect.y - self.vitesse
            else :
                self.game.active_musique = True
                self.game.GAME_OVER = True
                self.game.all_bucheron_C.empty()
                self.game.all_bucheron_H.empty()
                self.game.all_projectile.empty()
        if self.rect.y < self.game.arbre.rect.y :
            if not self.rect.colliderect(self.game.arbre.rect) :
                move_player_H(self)
                self.rect.y = self.rect.y + self.vitesse
            else :
                self.game.active_musique = True
                self.game.GAME_OVER = True
                self.game.all_bucheron_C.empty()
                self.game.all_bucheron_H.empty()
                self.game.all_projectile.empty()
