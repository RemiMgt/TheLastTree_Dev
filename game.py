import pygame
from player import Player
from map_jeux import Map
from arbre import Arbre
from bucheron_H import Bucheron_H
from bucheron_C import Bucheron_C
from projectile import Projectile

class Game() :
    def __init__(self) :
        self.player = Player(self)
        self.map = Map()
        self.arbre = Arbre(self)
        self.bucheron_H = Bucheron_H(self)
        self.bucheron_C = Bucheron_C(self)
        self.all_bucheron_H = pygame.sprite.Group()
        self.all_bucheron_V = pygame.sprite.Group()
        self.all_projectile = pygame.sprite.Group()
        self.pressed = {}

    def ajout_bucheron_H(self) :
        self.all_bucheron_H.add(Bucheron_H(self))

    def ajout_bucheron_C(self) :
        self.all_bucheron_C.add(Bucheron_C(self))

    def ajout_projectile(self, direction) :
        self.all_projectile.add(Projectile(self, direction))

    def check_collision(self, sprite, group) : #FOnction qui retrun True si il y a collision entre sprite et group
        return pygame.sprite.spritecollide(sprite, group, True, pygame.sprite.collide_mask) #sprite / group / Oui ou non détruire entité si il y a collision