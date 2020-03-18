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

    def update(self, dt):
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

class MovingBlock(object):
    def __init__(self, pos, size, startRange, endRange, color):
        self.pos = pos*24
        self.size = size*24
        self.hitBox = HitBox(self.pos, self.size, True, Layer("solid"), Vec2(50,0))
        self.startRange = self.pos[0] + startRange * 24
        self.endRange = self.pos[0] + endRange * 24
        self.color = color
        self.mainScreen = pygame.display.get_surface()
    def update(self, dt):
        self.move()
    def remove(self):
        self.hitBox.remove()
    def draw(self,surface):
        pygame.draw.rect(surface, self.color, (self.pos[0], self.pos[1], self.size[0], self.size[1]))
    def move(self):
        if self.startRange < self.endRange:
            if self.hitBox.pos.x < self.startRange:
                self.hitBox.vel.x = 50
            if self.hitBox.pos.x > self.endRange:
                self.hitBox.vel.x = -50
        if self.startRange > self.endRange:
            if self.hitBox.pos.x > self.startRange:
                self.hitBox.vel.x = -50
            if self.hitBox.pos.x < self.endRange:
                self.hitBox.vel.x = 50

    #def setvelocity(self, velocity):
    #    self.hitbox.vel = velocity
    #    pygame.draw.rect(self.screen, self.color, [self.position.x,self.position.y, self.size.x,self.size.y])
