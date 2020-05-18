import pygame, HitBox
from HitBox import *


class PowerUps(object):
        def __init__(self, pos, size, color):
            pos *= 24
            pos.y -= 8
            size *= 24
            self.hitBox = HitBox(pos, size, False, Layer("powerUps"))
            self.ShieldImage = pygame.image.load('Graphics/PowerUpGraphics/ShieldFrames/Shield.png')
            self.frame = 0
            self.mainScreen = pygame.display.get_surface()

        def update(self, game, dt):
            self.move()

        def remove(self):
            self.hitBox.remove()

        def draw(self,surface):
            surface.blit(self.ShieldImage,((self.hitBox.pos.x),self.hitBox.pos.y))
