from Vec2 import *
import pygame

class Camera:

    def __init__(self, size, background):
        self.position = Vec2()
        self.size = size
        self.background = background
        self.surface = pygame.Surface(self.size.values)
        self.mainScreen = pygame.display.get_surface()
        self.surface.fill(self.background)

    def draw(self):
        self.mainScreen.fill(self.background)
        self.surface.blit(self.mainScreen, self.position.values)
        self.surface.fill(self.background)

    def move(self, deltaPos):
        self.position += deltaPos

    def glide(self, target, glideFactor = 0.1):
        self.position += (target - self.position) * 0.1
