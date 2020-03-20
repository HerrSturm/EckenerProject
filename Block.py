#BlockClass
#21.01.2020
#Ole, Philippe

import sys, pygame
from Vec2 import Vec2
from HitBox import *

class Block(object):
    def __init__(self, position, size, color):
        super(Block, self).__init__()
        self.color = color
        self.screen = pygame.display.get_surface()
        self.hitBox = HitBox(position * 24, size * 24, True, Layer("solid"))

    def update(self, game, dt):
        pass

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, [self.hitBox.pos.values, self.hitBox.size.values])

    def remove(self):
        self.hitBox.remove()

class EndBlock(object):
    def __init__(self, position, size, color):
        self.color = color
        self.screen = pygame.display.get_surface()
        self.hitBox = HitBox(position * 24, size * 24, True, Layer("end"))

    def update(self, game, dt):
        pass

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, [self.hitBox.pos.values, self.hitBox.size.values])

    def remove(self):
        self.hitBox.remove()

class MovingBlock(object):
    def __init__(self, pos, size, startRange, endRange, color):
        self.hitBox = HitBox(pos * 24, size * 24, True, Layer("solid"), Vec2(50,0))
        self.startRange = self.hitBox.pos.x + startRange * 24
        self.endRange = self.hitBox.pos.x + endRange * 24
        self.color = color
        self.mainScreen = pygame.display.get_surface()
    def update(self, game, dt):
        self.move()
    def remove(self):
        self.hitBox.remove()
    def draw(self,surface):
        pygame.draw.rect(surface, self.color, (self.hitBox.pos.values, self.hitBox.size.values))
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
