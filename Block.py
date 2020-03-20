#BlockClass
#21.01.2020
#Ole, Philippe

import sys, pygame
from Vec2 import Vec2
from HitBox import *

class Block(object):
    def __init__(self, position, size, color, graphicID = "grass"):
        super(Block, self).__init__()
        self.size = size * 24
        self.position = position * 24
        self.color = color
        self.screen = pygame.display.get_surface()
        self.hitbox = HitBox(self.position,self.size, True, Layer("solid"))
        self.graphicID = graphicID

        if graphicID == "grass":
            self.graphicLeft = pygame.image.load("Graphics/Blocks/grass/leftCorner.png").convert_alpha()
            self.graphicLeft = pygame.transform.scale(self.graphicLeft, (24, 24))
            self.graphicMiddle = pygame.image.load("Graphics/Blocks/grass/middle.png").convert_alpha()
            self.graphicMiddle = pygame.transform.scale(self.graphicMiddle, (24, 24))
            self.graphicRight = pygame.image.load("Graphics/Blocks/grass/rightCorner.png").convert_alpha()
            self.graphicRight = pygame.transform.scale(self.graphicRight, (24, 24))
            self.graphicOneBlock = pygame.image.load("Graphics/Blocks/grass/oneBlock.png").convert_alpha()
            self.graphicOneBlock = pygame.transform.scale(self.graphicOneBlock, (24, 24))
        self.graphic = pygame.image.load("Graphics/Blocks/" + graphicID + ".png").convert_alpha()
        self.graphic = pygame.transform.scale(self.graphic, (24, 24))

    def update(self, dt):
        pass

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, [self.position.x,self.position.y, self.size.x,self.size.y])

        if self.graphicID == "grass" and self.size.y == 24:
            if self.size.x == 24:
                surface.blit(self.graphicOneBlock, (self.position.x, self.position.y))
            else:
                len = int(self.size.x / 24)
                for x in range(0, len):
                    if x == 0:
                        surface.blit(self.graphicLeft, (self.position.x + x*24, self.position.y))
                    elif x+1 == len:
                        surface.blit(self.graphicRight, (self.position.x + x*24, self.position.y))
                    else:
                        surface.blit(self.graphicMiddle, (self.position.x + x*24, self.position.y))
        else:
            for x in range(0, int(self.size.x / 24)):
                for y in range(0, int(self.size.y / 24)):
                    surface.blit(self.graphic, (self.position.x + x*24, self.position.y + y*24))

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
    def __init__(self, pos, size, startRange, endRange, color, graphicID = "grass"):
        self.pos = pos*24
        self.size = size*24
        self.hitBox = HitBox(self.pos, self.size, True, Layer("solid"), Vec2(50,0))
        self.startRange = self.pos[0] + startRange * 24
        self.endRange = self.pos[0] + endRange * 24
        self.color = color
        self.mainScreen = pygame.display.get_surface()
        self.graphic = pygame.image.load("Graphics/Blocks/" + graphicID + ".png").convert_alpha()
        self.graphic = pygame.transform.scale(self.graphic, (24, 24))

    def update(self, dt):
        self.move()

    def remove(self):
        self.hitBox.remove()

    def draw(self,surface):
        pygame.draw.rect(surface, self.color, (self.pos[0], self.pos[1], self.size[0], self.size[1]))
        for x in range(0, int(self.size.x / 24)):
            for y in range(0, int(self.size.y / 24)):
                surface.blit(self.graphic, (self.pos[0] + x*24, self.pos[1] + y*24))

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
