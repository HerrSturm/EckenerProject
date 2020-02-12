import pygame
from HitBox import *
class Character():
    def __init__(self):
        self.hitBox = HitBox(Vec2(50,50), Vec2(150,150), False, Layer("player"))
        self.mainScreen = pygame.display.get_surface()
        pygame.draw.rect(self.mainScreen, (255, 255, 255), (self.hitBox.pos.x, self.hitBox.pos.y, self.hitBox.size.x, self.hitBox.size.y))
    def update(self):
        pygame.draw.rect(self.mainScreen, (255, 255, 255), (self.hitBox.pos.x, self.hitBox.pos.y, self.hitBox.size.x, self.hitBox.size.y))
