import pygame, HitBox, Vec2
from HitBox import *
class Gegner(object):
    def __init__(self, pos, size, startRange, endRange):
        self.hitBox = HitBox(pos, size * 24, False, Layer("deadly"), Vec2(100,0))
        self.startRange = startRange
        self.endRange = endRange
        self.mainScreen = pygame.display.get_surface()
    def draw(self):
        pygame.draw.rect(self.mainScreen, (255, 255, 255), (self.hitBox.pos.values[0], self.hitBox.pos.values[1], self.hitBox.size.values[0], self.hitBox.size.values[1]))

    def move(self):
        if self.startRange < self.endRange:
            if self.hitBox.pos.x < self.startRange:
                self.hitBox.vel.x = 100
            if self.hitBox.pos.x > self.endRange:
                self.hitBox.vel.x = -100
        if self.startRange > self.endRange:
            if self.hitBox.pos.x > self.startRange:
                self.hitBox.vel.x = -100
            if self.hitBox.pos.x < self.endRange:
                self.hitBox.vel.x = 100
