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

    def remove(self) :
        self.game.all_projectile.remove(self) #Détruire le projectile courant

    def move(self) :
        if self.direction == "H" :
            if not self.game.check_collision(self, self.game.all_bucheron_H) and not self.game.check_collision(self, self.game.all_bucheron_C) :
                self.rect.y = self.rect.y - self.vitesse
            else :
                print("Collision / Suppression !")
                self.game.nombre_kill += 1
                self.remove()
        elif self.direction == "B" :
            if not self.game.check_collision(self, self.game.all_bucheron_H) and not self.game.check_collision(self, self.game.all_bucheron_C) :
                self.rect.y = self.rect.y + self.vitesse
            else :
                print("Collision / Suppression !")
                self.game.nombre_kill += 1
                self.remove()
        elif self.direction == "D" :
            if not self.game.check_collision(self, self.game.all_bucheron_H) and not self.game.check_collision(self, self.game.all_bucheron_C) :
                self.rect.x = self.rect.x + self.vitesse
            else :
                print("Collision / Suppression !")
                self.game.nombre_kill += 1
                self.remove()
        elif self.direction == "G" :
            if not self.game.check_collision(self, self.game.all_bucheron_H) and not self.game.check_collision(self, self.game.all_bucheron_C) :
                self.rect.x = self.rect.x - self.vitesse
            else :
                print("Collision / Suppression !")
                self.game.nombre_kill += 1
                self.remove()

    def move_player(self) :
        if self.game.player.direction == "D" :
            self.rect.x = self.rect.x - self.vitesse
        if self.game.player.direction == "G" :
            self.rect.x = self.rect.x + self.vitesse
        if self.game.player.direction == "H" :
            self.rect.y = self.rect.y + self.vitesse
        if self.game.player.direction == "B" :
            self.rect.y = self.rect.y - self.vitesse