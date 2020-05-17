import pygame
from player import Player
from map_jeux import Map
from arbre import Arbre

class Game() :
    def __init__(self) :
        self.player = Player(self)
        self.map = Map()
        self.arbre = Arbre()
        self.pressed = {}

    def check_collision(self, sprite, group) : #FOnction qui retrun True si il y a collision entre sprite et group
        return pygame.sprite.spritecollide(sprite, group, True, pygame.sprite.collide_mask) #sprite / group / Oui ou non détruire entité si il y a collision