from HitBox import *
import random

import sys, pygame
pygame.init()
mainScreenSize = width, height = 1200, 800
mainScreen = pygame.display.set_mode(mainScreenSize)

def drawHitBox(hitBox):
    pygame.draw.rect(mainScreen, pygame.Color("black"), pygame.Rect(hitBox.pos.values, hitBox.size.values))

hitBoxes = []

def collided(self, other):
    print(self, other)

for i in range(50):
    hitBox = None
    size = Vec2(random.random() * 50 + 20, random.random() * 50 + 20)
    while True:
        hitBox = HitBox(
            Vec2(random.random() * (mainScreenSize[0] - size.x),
                 random.random() * (mainScreenSize[1] - size.y)),
        size, False, #random.random() < 0.5,
        Layer("platform"))
        if any([h.overlap(hitBox) for h in hitBoxes]):
            hitBox.remove()
            del hitBox
            continue
        hitBoxes.append(hitBox)
        hitBox.onCollide(collided)
        break


def draw():
    mainScreen.fill(pygame.Color("white"))
    for hitBox in hitBoxes:
        drawHitBox(hitBox)

clock = pygame.time.Clock()

for hitBox in hitBoxes:
    hitBox.vel = Vec2((random.random() - 0.5) * 2 * 100, (random.random() - 0.5) * 2 * 100)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()

    dt = clock.get_time() / 1000.0
    clock.tick()

    CollisionManager().update(dt)

    draw()

    pygame.display.flip()
    #Shutdownhandling
    if keys[pygame.K_ESCAPE]:
        sys.exit()
