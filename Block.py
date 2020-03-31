#BlockClass
#21.01.2020
#Ole, Philippe

import sys, pygame
from Vec2 import Vec2
from HitBox import *
from sprites import endBlockSprites

class Block(object):
    def __init__(self, position, size, color, graphicID = "grass"):
        super(Block, self).__init__()
        self.color = color
        self.screen = pygame.display.get_surface()
        self.hitBox = HitBox(position * 24, size * 24, True, Layer("solid"))
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
            self.graphicTop = pygame.image.load("Graphics/Blocks/grass/top.png").convert_alpha()
            self.graphicTop = pygame.transform.scale(self.graphicTop, (24, 24))
        self.graphic = pygame.image.load("Graphics/Blocks/" + graphicID + ".png").convert_alpha()
        self.graphic = pygame.transform.scale(self.graphic, (24, 24))

    def update(self, game, dt):
        pass

    def draw(self, surface):

        if self.graphicID == "grass" and self.hitBox.size.y == 24:
            if self.hitBox.size.x == 24:
                surface.blit(self.graphicTop, (self.hitBox.pos.x, self.hitBox.pos.y-17))
                surface.blit(self.graphicOneBlock, (self.hitBox.pos.x, self.hitBox.pos.y))
            else:
                len = int(self.hitBox.size.x / 24)
                for x in range(0, len):
                    if x == 0:
                        surface.blit(self.graphicTop, (self.hitBox.pos.x + x*24, self.hitBox.pos.y-17))
                        surface.blit(self.graphicLeft, (self.hitBox.pos.x + x*24, self.hitBox.pos.y))
                    elif x+1 == len:
                        surface.blit(self.graphicTop, (self.hitBox.pos.x + x*24, self.hitBox.pos.y-17))
                        surface.blit(self.graphicRight, (self.hitBox.pos.x + x*24, self.hitBox.pos.y))
                    else:
                        surface.blit(self.graphicTop, (self.hitBox.pos.x + x*24, self.hitBox.pos.y-19))
                        surface.blit(self.graphicMiddle, (self.hitBox.pos.x + x*24, self.hitBox.pos.y))
        else:
            for x in range(0, int(self.hitBox.size.x / 24)):
                for y in range(0, int(self.hitBox.size.y / 24)):
                    surface.blit(self.graphic, (self.hitBox.pos.x + x*24, self.hitBox.pos.y + y*24))

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
    def __init__(self, pos, size, startRange, endRange, color, graphicID = "grass"):
        self.hitBox = HitBox(pos * 24, size * 24, True, Layer("solid"), Vec2(50,0))
        self.startRange = self.hitBox.pos.x + startRange * 24
        self.endRange = self.hitBox.pos.x + endRange * 24
        self.color = color
        self.mainScreen = pygame.display.get_surface()
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
            self.graphicTop = pygame.image.load("Graphics/Blocks/grass/top.png").convert_alpha()
            self.graphicTop = pygame.transform.scale(self.graphicTop, (24, 24))
        self.graphic = pygame.image.load("Graphics/Blocks/" + graphicID + ".png").convert_alpha()
        self.graphic = pygame.transform.scale(self.graphic, (24, 24))

    def update(self, game, dt):
        self.move()

    def remove(self):
        self.hitBox.remove()

    def draw(self,surface):
        if self.graphicID == "grass" and self.hitBox.size.y == 24:
            if self.hitBox.size.x == 24:
                surface.blit(self.graphicTop, (self.hitBox.pos.x, self.hitBox.pos.y-17))
                surface.blit(self.graphicOneBlock, (self.hitBox.pos.x, self.hitBox.pos.y))
            else:
                len = int(self.hitBox.size.x / 24)
                for x in range(0, len):
                    if x == 0:
                        surface.blit(self.graphicTop, (self.hitBox.pos.x + x*24, self.hitBox.pos.y-17))
                        surface.blit(self.graphicLeft, (self.hitBox.pos.x + x*24, self.hitBox.pos.y))
                    elif x+1 == len:
                        surface.blit(self.graphicTop, (self.hitBox.pos.x + x*24, self.hitBox.pos.y-17))
                        surface.blit(self.graphicRight, (self.hitBox.pos.x + x*24, self.hitBox.pos.y))
                    else:
                        surface.blit(self.graphicTop, (self.hitBox.pos.x + x*24, self.hitBox.pos.y-19))
                        surface.blit(self.graphicMiddle, (self.hitBox.pos.x + x*24, self.hitBox.pos.y))
        else:
            for x in range(0, int(self.hitBox.size.x / 24)):
                for y in range(0, int(self.hitBox.size.y / 24)):
                    surface.blit(self.graphic, (self.hitBox.pos.x + x*24, self.hitBox.pos.y + y*24))
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
