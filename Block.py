#BlockClass
#21.01.2020
#Ole, Philippe

import sys, pygame
from Vec2 import Vec2
from HitBox import *

class Block(object):
    def __init__(self, size, position, color):
        super(block, self).__init__()
        self.size = Vec2(size[0]*24,size[1]*24)
        self.position = Vec2(position[0]*24,position[1]*24)
        self.color = color
        self.screen = pygame.display.get_surface()
        self.hitbox = HitBox(self.position,self.size, True, Layer("solid"))
        pygame.draw.rect(self.screen, self.color, [self.position[0],self.position[1], self.size[0],self.size[1]])

    def update(self):
        pygame.draw.rect(self.screen, self.color, [self.position[0],self.position[1], self.size[0],self.size[1]])

    def move(self,position):
        self.position = (self.position[0]+position[0],self.position[1]+position[1])
        pygame.draw.rect(self.screen, self.color, [self.position[0],self.position[1], self.size[0],self.size[1]])
