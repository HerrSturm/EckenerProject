import pygame
from HitBox import*
class Character():
    def __init__(self):
        self.hitBox = HitBox(Vec2(50,50), Vec2(150,150), False, Layer("player"), Vec2(0,5, 0))
        self.mainScreen = pygame.display.get_surface()
        pygame.draw.rect(self.mainScreen, (255, 255, 255), (self.hitBox.pos.values[0], self.hitBox.pos.values[1], self.hitBox.size.values[0], self.hitBox.size.values[1]))
    def update(self):
        pygame.draw.rect(self.mainScreen, self.shape)
