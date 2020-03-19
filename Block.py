#BlockClass
#21.01.2020
#Ole, Philippe

import sys, pygame
from Vec2 import Vec2
from HitBox import *

class Block(object):
    def __init__(self, position, size, color):
        super(Block, self).__init__()
        self.size = size * 24
        self.position = position * 24
        self.color = color
        self.screen = pygame.display.get_surface()
        self.hitbox = HitBox(self.position,self.size, True, Layer("solid"))

    def update(self, game, dt):
        pass

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, [self.position.x,self.position.y, self.size.x,self.size.y])

    def remove(self):
        self.hitbox.remove()

    def move(self,position):
        self.position += position

class EndBlock(object):
    def __init__(self, position, size, color):
        self.size = size * 24
        self.position = position * 24
        self.color = color
        self.screen = pygame.display.get_surface()
        self.hitbox = HitBox(self.position,self.size, True, Layer("end"))

    def update(self, dt):
        pass

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, [self.position.x,self.position.y, self.size.x,self.size.y])

    def remove(self):
        self.hitbox.remove()

    def move(self,position):
        self.position += position

    #def setvelocity(self, velocity):
    #    self.hitbox.vel = velocity
    #    pygame.draw.rect(self.screen, self.color, [self.position.x,self.position.y, self.size.x,self.size.y])
