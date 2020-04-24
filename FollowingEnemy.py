import pygame, HitBox, Vec2
from GegnerClass import *
from HitBox import *

class FollowingEnemy(Gegner):
    def __init__(self, pos, size, startrange, endrange):
        super().__init__(pos, size, startrange, endrange)
        #pos.y += 400
        self.hitBox = HitBox(pos, Vec2(55,40), False, Layer("deadly"), Vec2(100,0))
        self.FlugAnimationBat = [pygame.transform.scale(pygame.image.load("Graphics/EnemyGraphics/Bat/BatFrames/BatFrame1.png"), (120, 105)),
                            pygame.transform.scale(pygame.image.load("Graphics/EnemyGraphics/Bat/BatFrames/BatFrame2.png"), (120, 105)),
                            pygame.transform.scale(pygame.image.load("Graphics/EnemyGraphics/Bat/BatFrames/BatFrame3.png"), (120, 105)),
                            pygame.transform.scale(pygame.image.load("Graphics/EnemyGraphics/Bat/BatFrames/BatFrame4.png"), (120, 105))]

    def draw(self,surface):
        pygame.draw.rect(surface, (255, 255, 255), (self.hitBox.pos.values[0], self.hitBox.pos.values[1], self.hitBox.size.values[0], self.hitBox.size.values[1]))
        self.enemy = self.FlugAnimationBat[(self.frame//50)%len(self.FlugAnimationBat)-4]
        if self.hitBox.vel.x < 0:
            self.enemy = pygame.transform.flip(self.enemy,True,False)
        surface.blit(self.enemy,(self.hitBox.pos.x -34,self.hitBox.pos.y -30))
