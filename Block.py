#BlockClass
#21.01.2020
#Ole, Philippe

import sys, pygame
from Vec2 import Vec2
from HitBox import *

class Block(object):
    def __init__(self, size, position, color):
        super(Block, self).__init__()
        self.size = size * 24
        self.position = position * 24
        self.color = color
        self.screen = pygame.display.get_surface()
        self.hitbox = HitBox(self.position,self.size, True, Layer("solid"))
        pygame.draw.rect(self.screen, self.color, [self.position[0],self.position[1], self.size[0],self.size[1]])

    def update(self):
        pygame.draw.rect(self.screen, self.color, [self.position[0],self.position[1], self.size[0],self.size[1]])

    def move(self,position):
        self.position += position
        pygame.draw.rect(self.screen, self.color, [self.position[0],self.position[1], self.size[0],self.size[1]])
