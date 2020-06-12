import pygame, HitBox
from HitBox import *
from Character import *

class Shield(object):
        def __init__(self, pos, size, color):
            pos *= 24
            pos.y -= 8
            size *= 24
            self.shieldHitBox = HitBox(pos, size, False, Layer("powerUps"))
            self.shieldImage = pygame.image.load('Graphics/GUI/shield.png')
            self.shieldHitBox.onCollide(self.remove, Layer("player"))
            self.shieldRemove = False

        def update(self, game, dt):
            if self.shieldRemove:
                game.currentLevel.objects.remove(self)
                self.shieldHitBox.remove()

        def remove(self, hitbox, other, dir, layer):
            self.shieldRemove = True

        def draw(self,surface):
            surface.blit(self.shieldImage,((self.shieldHitBox.pos.x),self.shieldHitBox.pos.y))

class JumpBoost(Shield):
        def __init__(self, pos, size, color):
            pos *= 24
            pos.y -= 8
            size *= 24
            self.jumpBoostHitBox = HitBox(pos, size, False, Layer("powerUps"))
            self.jumpBoostImage = pygame.image.load('Graphics/GUI/jumpboost.png')
            self.jumpBoostHitBox.onCollide(self.remove, Layer("player"))
        def update(self, game, dt):
            if self.jumpBoostRemove:
                game.currentLevel.objects.remove(self)
                self.jumpBoostHitBox.remove()

        def remove(self, hitbox, other, dir, layer):
            self.jumpBoostRemove = True

        def draw(self,surface):
            surface.blit(self.jumpBoostImage,((self.jumpBoostHitBox.pos.x),self.jumpBoostHitBox.pos.y))
