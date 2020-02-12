import sys, pygame, time
from Block import Block
from Vec2 import Vec2
from characterClass import Character
from CollisionManager import CollisionManager
from GegnerClass import *
pygame.init()

brown = (150,80,50)
blue = (80,150,255)
green = (50,100,50)


size = width, heigth = 1400, 800
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.flip()

screen.fill((80,150,255))

b1 = Block(Vec2(10, 10), Vec2(0,26), brown)
b2 = Block(Vec2(10, 1), Vec2(0,25), green)
b3 = Block(Vec2(10, 20), Vec2(14,20), brown)
b4 = Block(Vec2(10, 1), Vec2(14,19), green)
b5 = Block(Vec2(5, 1), Vec2(30,19), brown)
b6 = Block(Vec2(5, 1), Vec2(30,18), green)
b7 = Block(Vec2(30, 20), Vec2(37,23), brown)
b8 = Block(Vec2(30, 1), Vec2(37,22), green)

tom = Character()

gegner = Gegner(Vec2(50,300),100, 600)


while True:
    screen.fill((80,150,255))
    gegner.move()
    gegner.draw()
    tom.draw()
    b1.update()
    b2.update()
    b3.update()
    b4.update()
    b5.update()
    b6.update()
    b7.update()
    b8.update()
    #handles the shutting down of the programm, ignorieren!
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]==False and keys[pygame.K_d]==False:
        tom.standstill()
    if keys[pygame.K_a]:
        tom.moveleft()
    if keys[pygame.K_d]:
        tom.moveright()

    dt = clock.get_time() / 1000.0
    clock.tick(60) # Kontrolliert die Aktuallisierungen pro Minute (FPS)

    CollisionManager().update(dt)

    pygame.display.flip()
