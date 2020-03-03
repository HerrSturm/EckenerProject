from Vec2 import *
import pygame

class Camera:
    DEFAULT_GLIDE_FACTOR = 1

    def __init__(self, size, background):
        self.position = Vec2()
        self.size = size
        self.background = background
        self.surface = pygame.Surface(self.size.values)
        self.mainScreen = pygame.display.get_surface()
        self.surface.fill(self.background)

    def draw(self):
        self.mainScreen.fill(self.background)
        self.mainScreen.blit(self.surface, self.position.values)
        self.surface.fill(self.background)

    def moveTo(self, position):
        self.position = -position

    def moveToCenter(self, position):
        self.position = -(position - Vec2(*self.mainScreen.get_size()) / 2)

    def glide(self, target, dt, glideFactor = DEFAULT_GLIDE_FACTOR):
        self.position += (target - self.position) * dt * glideFactor

    def glideCenter(self, target, dt, glideFactor = DEFAULT_GLIDE_FACTOR):
        self.glide(-(target - Vec2(*self.mainScreen.get_size()) / 2), dt, glideFactor)
