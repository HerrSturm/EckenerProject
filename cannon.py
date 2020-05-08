import pygame, HitBox, Vec2
from GegnerClass import *
from HitBox import *

#Cannon Klasse durch Oberklasse erstellt
class Cannon(object):
    def __init__(self, pos, size):
        pos *= 24
        size *= 24
        self.hitBox = HitBox(pos, Vec2(55,50), True, Layer("solid"))
        self.mainScreen = pygame.display.get_surface()
        self.img = 0
        self.cannonGraphic = pygame.transform.scale(pygame.image.load("Graphics/EnemyGraphics/cannon/cannonTransFlipped.png"), (70, 55))

    def update(self, game, dt):
        self.move(game)


    def remove(self):
        self.hitBox.remove()

    def draw(self,surface):
        #pygame.draw.rect(surface, (255, 255, 255), (self.hitBox.pos.values[0], self.hitBox.pos.values[1], self.hitBox.size.values[0], self.hitBox.size.values[1]))
        self.enemy = self.cannonGraphic
        surface.blit(self.enemy,((self.hitBox.pos.x) -8,(self.hitBox.pos.y) -3))

    def move (self, game):
        self.hitBox.vel.x = 0


class CannonBall(object):
    def __init__(self, pos, size, startRange, endRange):
        pos *= 24
        size *= 24
        pos.x -= 50
        pos.y += 10
        self.hitBox = HitBox(pos, Vec2(31,31), False, Layer("Deadly"))
        self.startRange = pos.x + startRange * 24
        self.endRange = pos.x + endRange * 24
        self.halfRange = (self.endRange/2)
        self.mainScreen = pygame.display.get_surface()
        self.img = 0
        self.cannonBallGraphic = pygame.transform.scale(pygame.image.load("Graphics/EnemyGraphics/cannon/cannonBallTrans.png"), (45, 35))

    def update(self, game, dt):
        self.move(game)


    def remove(self):
        self.hitBox.remove()

    def draw(self, surface):
        #pygame.draw.rect(surface, (255, 255, 255), (self.hitBox.pos.values[0], self.hitBox.pos.values[1], self.hitBox.size.values[0], self.hitBox.size.values[1]))
        self.enemy = self.cannonBallGraphic
        surface.blit(self.enemy,((self.hitBox.pos.x) -8,(self.hitBox.pos.y) -3))

    def move(self, game):
        if self.hitBox.pos.x > self.halfRange:
            self.hitBox.vel = Vec2(-100, -100)
            #print("1")
        if self.hitBox.pos.x < self.halfRange:
            self.hitBox.vel = Vec2(-100, 100)
            #print("2")
        #if self.hitBox.pos.x < self.startRange:
            #print("lol")
