import pygame, HitBox, Vec2
from HitBox import *


class Gegner(object):
    def __init__(self, pos, size, startRange, endRange):
        pos *= 24
        pos.y -= 8
        size *= 24
        self.hitBox = HitBox(pos, Vec2(55,55), False, Layer("deadly"), Vec2(100,0))
        self.hitBox.onCollide(self.hitRemove, Layer("player"))
        self.hitRemove == False
        self.startRange = pos.x + startRange * 24
        self.endRange = pos.x + endRange * 24
        self.frame = 0
        self.mainScreen = pygame.display.get_surface()

        #self.enemy = [
            #pygame.image.load("Graphics/EnemyGraphics/observer/AnimationRechts/observerRight1.png").convert_alpha(),
            #pygame.image.load("Graphics/EnemyGraphics/observer/AnimationLinks/observerLeft1.png").convert_alpha()]
        self.img = 0

        #lädt Grafiken des Gegners
        self.LaufAnimationGoblin = [pygame.transform.scale(pygame.image.load("Graphics/EnemyGraphics/Goblin/GoblinFrames/runRight/frame1.png"), (70, 55)),
                            pygame.transform.scale(pygame.image.load("Graphics/EnemyGraphics/Goblin/GoblinFrames/runRight/frame2.png"), (70, 55)),
                            pygame.transform.scale(pygame.image.load("Graphics/EnemyGraphics/Goblin/GoblinFrames/runRight/frame3.png"), (70, 55)),
                            pygame.transform.scale(pygame.image.load("Graphics/EnemyGraphics/Goblin/GoblinFrames/runRight/frame4.png"), (70, 55)),
                            pygame.transform.scale(pygame.image.load("Graphics/EnemyGraphics/Goblin/GoblinFrames/runRight/frame5.png"), (70, 55)),
                            pygame.transform.scale(pygame.image.load("Graphics/EnemyGraphics/Goblin/GoblinFrames/runRight/frame6.png"), (70, 55)),
                            pygame.transform.scale(pygame.image.load("Graphics/EnemyGraphics/Goblin/GoblinFrames/runRight/frame7.png"), (70, 55)),
                            pygame.transform.scale(pygame.image.load("Graphics/EnemyGraphics/Goblin/GoblinFrames/runRight/frame8.png"), (70, 55))]

    #führt move Methode wiederholt durch
    def update(self, game, dt):
        self.move(game)
        if self.hitRemove == True:
                game.currentLevel.objects.remove(self)
                self.hitBox.remove()

    def hitRemove(self, hitBox, other, dir, layer):
        #if Direction == up:
        self.hitRemove = True

    def remove (self):
        self.hitBox.remove()


    #legt Grafik für Gegner fest
    def draw(self,surface):
        #pygame.draw.rect(surface, (255, 255, 255), (self.hitBox.pos.values[0], self.hitBox.pos.values[1], self.hitBox.size.values[0], self.hitBox.size.values[1]))
        self.enemy = self.LaufAnimationGoblin[(self.frame//50)%len(self.LaufAnimationGoblin)-4]
        if self.hitBox.vel.x < 0:
            self.enemy = pygame.transform.flip(self.enemy,True,False)
        surface.blit(self.enemy,((self.hitBox.pos.x) -8,self.hitBox.pos.y))

    #Funktion damit der Gegner sich bewegt
    def move(self, game):
        if self.startRange < self.endRange:
            if self.hitBox.pos.x < self.startRange:
                self.hitBox.vel.x = 100
            self.frame = self.frame + 4
            if self.hitBox.pos.x > self.endRange:
                self.hitBox.vel.x = -100
            self.frame = self.frame + 4
            if self.hitBox.vel.x == 0:
                if self.hitBox.pos.x > game.currentLevel.character.hitBox.pos.x:
                    self.hitBox.vel.x = 100
                if self.hitBox.pos.x < game.currentLevel.character.hitBox.pos.x:
                    self.hitBox.vel.x = -100
        if self.startRange > self.endRange:
            if self.hitBox.pos.x > self.startRange:
                self.hitBox.vel.x = -100
            self.frame = self.frame + 4
            if self.hitBox.pos.x < self.endRange:
                self.hitBox.vel.x = 100
            self.frame = self.frame + 4
            if self.hitBox.vel.x == 0:
                if self.hitBox.pos.x > game.currentLevel.character.hitBox.pos.x:
                    self.hitBox.vel.x = 100
                if self.hitBox.pos.x < game.currentLevel.character.hitBox.pos.x:
                    self.hitBox.vel.x = -100
