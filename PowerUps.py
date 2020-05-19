import pygame, HitBox
from HitBox import *
from Character import *

class PowerUps(object):
        def __init__(self, pos, size, color):
            pos *= 24
            pos.y -= 8
            size *= 24
            self.hitBox = HitBox(pos, size, False, Layer("powerUps"))
            self.ShieldImage = pygame.image.load('Graphics/GUI/shield.png')
            self.hitBox.onCollide(self.remove, Layer("player"))
            self.remove = False

        def update(self, game, dt):
            if self.remove:
                game.currentLevel.objects.remove(self)
                self.hitBox.remove()

        def remove(self, hitbox, other, dir, layer, game):
            self.remove = True

        def draw(self,surface):
            surface.blit(self.ShieldImage,((self.hitBox.pos.x),self.hitBox.pos.y))
