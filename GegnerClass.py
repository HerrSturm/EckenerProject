import pygame, HitBox, Vec2
from HitBox import *

<<<<<<< HEAD
LaufAnimationEye = [pygame.image.load("Graphics/EnemyGraphics/observer/AnimationRechts/observerRight1.png"),
                    pygame.image.load("Graphics/EnemyGraphics/observer/AnimationRechts/observerRight2.png"),
                    pygame.image.load("Graphics/EnemyGraphics/observer/AnimationRechts/observerRight3.png")]

LaufAnimationChicken = [pygame.image.load("Graphics/EnemyGraphics/chicken/ausgeschnitten/chicken1.png"),
                    pygame.image.load("Graphics/EnemyGraphics/chicken/ausgeschnitten/chicken2.png"),
                    pygame.image.load("Graphics/EnemyGraphics/chicken/ausgeschnitten/chicken3.png"),
                    pygame.image.load("Graphics/EnemyGraphics/chicken/ausgeschnitten/chicken4.png")]
=======
>>>>>>> master

class Gegner(object):
    def __init__(self, pos, size, startRange, endRange):
        global LaufAnimationEye
        pos *= 24
        pos.y -= 8
        size *= 24
        self.hitBox = HitBox(pos, Vec2(55,55), False, Layer("deadly"), Vec2(100,0))
        self.startRange = pos.x + startRange * 24
        self.endRange = pos.x + endRange * 24
        self.frame = 0
        self.mainScreen = pygame.display.get_surface()
<<<<<<< HEAD
        self.LaufAnimationRight = LaufAnimationEye
        self.enemy = self.LaufAnimationRight[0].convert_alpha()
        self.img = 0

=======

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
>>>>>>> master

    #führt move Methode wiederholt durch
    def update(self, game, dt):
        self.move(game)

    def remove(self):
        self.hitBox.remove()

    #legt Grafik für Gegner fest
    def draw(self,surface):
        #pygame.draw.rect(surface, (255, 255, 255), (self.hitBox.pos.values[0], self.hitBox.pos.values[1], self.hitBox.size.values[0], self.hitBox.size.values[1]))
<<<<<<< HEAD
<<<<<<< HEAD
        self.enemy = self.LaufAnimationRight[(self.frame//50)%len(self.LaufAnimationRight)-1].convert_alpha()
=======
        self.enemy = self.LaufAnimationGoblin[(self.frame//50)%len(self.LaufAnimationGoblin)-2]
>>>>>>> master
=======
        self.enemy = self.LaufAnimationGoblin[(self.frame//50)%len(self.LaufAnimationGoblin)-4]
>>>>>>> master
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
<<<<<<< HEAD
<<<<<<< HEAD
            self.frame = self.frame + 1


class TeleportingChicken(Gegner):
    def __init__(self, pos, size, startRange, endRange):
        global LaufAnimationChicken
        super().__init__(pos, size, startRange, endRange)
        self.LaufAnimationRight = LaufAnimationChicken


    def move(self):
        if self.hitBox.vel.x == 0:
            self.hitBox.vel.x = 100
        if self.startRange < self.endRange:
            if self.hitBox.pos.x > self.endRange:
                self.hitBox.pos.x = self.startRange
            self.frame = self.frame + 5
=======
            self.frame = self.frame + 2
>>>>>>> master
=======
            self.frame = self.frame + 4
            if self.hitBox.vel.x == 0:
                if self.hitBox.pos.x > game.currentLevel.character.hitBox.pos.x:
                    self.hitBox.vel.x = 100
                if self.hitBox.pos.x < game.currentLevel.character.hitBox.pos.x:
                    self.hitBox.vel.x = -100
>>>>>>> master
