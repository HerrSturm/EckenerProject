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
        pos.x -= 30
        pos.y -= 20
        self.startPos = pos
        self.hitBox = HitBox(pos, Vec2(31,31), False, Layer("deadly"))
        self.hitBox.onCollide(self.respawn, Layer("player"))
        self.hitBox.onCollide(self.respawn, Layer("solid"))
        self.startRange = startRange * 24
        self.endRange = endRange * 24
        self.halfRange = (self.startRange/2 + self.endRange/2)
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
        #print(self.startRange, self.halfRange, self.endRange)
        #print(game.currentLevel.character.hitBox.pos)
        #print(self.hitBox.vel.x)
        #print(self.hitBox.pos)
        print(self.startPos)
        if self.hitBox.pos.x > self.halfRange:
            self.hitBox.vel = Vec2(-150, -125)
        if self.hitBox.pos.x < self.halfRange and self.hitBox.pos.x > self.endRange:
            self.hitBox.vel = Vec2(-150, 125)

    def respawn(self, hitbox, other, dir, layer):
        self.hitBox.pos.x = self.startPos.x
        self.hitBox.pos.y = self.startPos.y
