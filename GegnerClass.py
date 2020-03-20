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
        self.enemy = [
            pygame.image.load("Graphics/EnemyGraphics/observer/AnimationRechts/observerRight1.png").convert_alpha(),
            pygame.image.load("Graphics/EnemyGraphics/observer/AnimationLinks/observerLeft1.png").convert_alpha()]
        self.img = 0


    def update(self, dt):
        self.move()

    def remove(self):
        self.hitBox.remove()

    def draw(self,surface):
        #pygame.draw.rect(self.mainScreen, (255, 255, 255), (self.hitBox.pos.values[0], self.hitBox.pos.values[1], self.hitBox.size.values[0], self.hitBox.size.values[1]))
        surface.blit(self.enemy[self.img],(self.hitBox.pos.x,self.hitBox.pos.y))
    def move(self):
        if self.startRange < self.endRange:
            if self.hitBox.pos.x < self.startRange:
                self.hitBox.vel.x = 100
                self.img=0
            if self.hitBox.pos.x > self.endRange:
                self.hitBox.vel.x = -100
                self.img=1
        if self.startRange > self.endRange:
            if self.hitBox.pos.x > self.startRange:
                self.hitBox.vel.x = -100
                self.img=1
            if self.hitBox.pos.x < self.endRange:
                self.hitBox.vel.x = 100
                self.img=0
