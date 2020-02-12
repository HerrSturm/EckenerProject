import sys, pygame, characterClass, HitBox, Vec2
from GegnerClass import *
pygame.init()
mainScreenSize = width, height = 1280, 720
mainScreen = pygame.display.set_mode(mainScreenSize)
character=characterClass.Character()
gegner = Gegner(Vec2(50,50),80, 800)
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    mainScreen.fill(pygame.Color(0,0,0))
    gegner.draw()
    gegner.move()
    pygame.display.flip()
    #Shutdownhandling
    if keys[pygame.K_ESCAPE]:
        sys.exit()

    dt = clock.get_time() / 1000.0
    CollisionManager().update(dt)
