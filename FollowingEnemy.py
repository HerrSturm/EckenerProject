import pygame, HitBox, Vec2
from GegnerClass import *
from HitBox import *

class FollowingEnemy(Gegner):
    def __init__(self, pos, size, startrange, endrange):
        super().__init__(pos, size, startrange, endrange)
        self.FlugAnimationObserver = [pygame.transform.scale(pygame.image.load("Graphics/EnemyGraphics/observer/AnimationRechts/observerRight1.png"), (70, 55)),
                            pygame.transform.scale(pygame.image.load("Graphics/EnemyGraphics/observer/AnimationRechts/observerRight2.png"), (70, 55)),
                            pygame.transform.scale(pygame.image.load("Graphics/EnemyGraphics/observer/AnimationRechts/observerRight3.png"), (70, 55))]

    def draw(self,surface):
        #pygame.draw.rect(surface, (255, 255, 255), (self.hitBox.pos.values[0], self.hitBox.pos.values[1], self.hitBox.size.values[0], self.hitBox.size.values[1]))
        self.enemy = self.FlugAnimationObserver[(self.frame//50)%len(self.FlugAnimationObserver)-3]
        if self.hitBox.vel.x < 0:
            self.enemy = pygame.transform.flip(self.enemy,True,False)
        surface.blit(self.enemy,((self.hitBox.pos.x) -8,self.hitBox.pos.y))
