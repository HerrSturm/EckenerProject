#BlockClass
#21.01.2020
#Ole, Philippe

import sys, pygame, Vec2
from HitBox import *

class block(object):
    def __init__(self, size, position, color):
        super(block, self).__init__()
        self.size = Vec2(size[0]*24,size[1]*24)
        self.position = Vec2(position[0]*24,position[1]*24)
        self.color = color
        self.screen = pygame.display.get_surface()
        self.hitbox = HitBox(Vec2(self.position[0],self.position[1])),Vec2(self.length,self.height), True, Layer("platform"))
        pygame.draw.rect(self.screen, self.color, [self.position[0],self.position[1], self.size])

    def update(self):
        pygame.draw.rect(self.screen, self.color, [self.position[0],self.position[1], self.size])

    def move(self,position):
        self.position = (self.position+position[0]*24,self.position+postition[1]*24)
        pygame.draw.rect(self.screen, self.color, [self.position[0],self.position[1], self.size])
