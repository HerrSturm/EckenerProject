import pygame, HitBox, Vec2
from HitBox import *
class Gegner(object):
    def __init__(self, pos, size, startRange, endRange):
        pos *= 24
        size *= 24
        self.hitBox = HitBox(pos, size, False, Layer("deadly"), Vec2(100,0))
        self.startRange = pos.x + startRange * 24
        self.endRange = pos.x + endRange * 24
        self.mainScreen = pygame.display.get_surface()
        self.enemy = pygame.image.load("Graphics/EnemyGraphics/observer/AnimationRechts/observerRight1.png").convert_alpha()


    def update(self, dt):
        self.move()

    def remove(self):
        self.hitBox.remove()

    def draw(self,surface):
        #pygame.draw.rect(self.mainScreen, (255, 255, 255), (self.hitBox.pos.values[0], self.hitBox.pos.values[1], self.hitBox.size.values[0], self.hitBox.size.values[1]))
        surface.blit(self.enemy,(self.hitBox.pos.x,self.hitBox.pos.y))
        print(self.hitBox.pos.values)
    def move(self):
        if self.startRange < self.endRange:
            if self.hitBox.pos.x < self.startRange:
                self.hitBox.vel.x = 100
                self.enemy = pygame.image.load("Graphics/EnemyGraphics/observer/AnimationRechts/observerRight1.png").convert_alpha()
            if self.hitBox.pos.x > self.endRange:
                self.hitBox.vel.x = -100
                self.enemy = pygame.image.load("Graphics/EnemyGraphics/observer/AnimationLinks/observerLeft1.png").convert_alpha()
        if self.startRange > self.endRange:
            if self.hitBox.pos.x > self.startRange:
                self.hitBox.vel.x = -100
                self.enemy = pygame.image.load("Graphics/EnemyGraphics/observer/AnimationLinks/observerLeft1.png").convert_alpha()
            if self.hitBox.pos.x < self.endRange:
                self.hitBox.vel.x = 100
                self.enemy = pygame.image.load("Graphics/EnemyGraphics/observer/AnimationRechts/observerRight1.png").convert_alpha()
