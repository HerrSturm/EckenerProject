import pygame, HitBox, Vec2
from GegnerClass import *
from HitBox import *

class FollowingEnemy(Gegner):
    def __init__(self, pos, size, startrange, endrange):
        super().__init__(pos, size, startrange, endrange)
        self.hitBox.size = Vec2(53,40)
        self.FlugAnimationBat = [pygame.transform.scale(pygame.image.load("Graphics/EnemyGraphics/Bat/BatFrames/BatFrame1.png"), (120, 105)),
                            pygame.transform.scale(pygame.image.load("Graphics/EnemyGraphics/Bat/BatFrames/BatFrame2.png"), (120, 105)),
                            pygame.transform.scale(pygame.image.load("Graphics/EnemyGraphics/Bat/BatFrames/BatFrame3.png"), (120, 105)),
                            pygame.transform.scale(pygame.image.load("Graphics/EnemyGraphics/Bat/BatFrames/BatFrame4.png"), (120, 105))]

        self.FlugAnimationBatFlipped = [pygame.transform.scale(pygame.image.load("Graphics/EnemyGraphics/Bat/BatFrames/BatFrameFlipped1.png"), (120, 105)),
                            pygame.transform.scale(pygame.image.load("Graphics/EnemyGraphics/Bat/BatFrames/BatFrameFlipped2.png"), (120, 105)),
                            pygame.transform.scale(pygame.image.load("Graphics/EnemyGraphics/Bat/BatFrames/BatFrameFlipped3.png"), (120, 105)),
                            pygame.transform.scale(pygame.image.load("Graphics/EnemyGraphics/Bat/BatFrames/BatFrameFlipped4.png"), (120, 105))]

    def draw(self,surface):
        #pygame.draw.rect(surface, (255, 255, 255), (self.hitBox.pos.values[0], self.hitBox.pos.values[1], self.hitBox.size.values[0], self.hitBox.size.values[1]))
        if self.hitBox.vel.x > 0:
            self.enemy = self.FlugAnimationBat[(self.frame//50)%len(self.FlugAnimationBat)-4]
        if self.hitBox.vel.x < 0:
            self.enemy = self.FlugAnimationBatFlipped[(self.frame//50)%len(self.FlugAnimationBatFlipped)-4]
        surface.blit(self.enemy,(self.hitBox.pos.x -34,self.hitBox.pos.y -30))

    def move(self, game):
        if game.currentLevel.character.hitBox.pos.x < self.hitBox.pos.x:
            self.hitBox.vel.x = -80
            self.frame = self.frame + 4
        if game.currentLevel.character.hitBox.pos.y < self.hitBox.pos.y:
            self.hitBox.vel.y = -50
        if game.currentLevel.character.hitBox.pos.x > self.hitBox.pos.x:
            self.hitBox.vel.x = 80
            self.frame = self.frame + 4
        if game.currentLevel.character.hitBox.pos.y > self.hitBox.pos.y:
            self.hitBox.vel.y = 50
