import sys, pygame, time
from Block import Block
from Vec2 import Vec2
from characterClass import Character
from CollisionManager import CollisionManager
from GegnerClass import *
pygame.init()

# Variabeln für Farben werden kreiert
brown = (150,80,50)
blue = (80,150,255)
green = (50,100,50)

# Pygame wird initialisiert
size = width, heigth = 1400, 800
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.flip()

screen.fill((80,150,255))

# Alle Blöcke werden mit Größe, Position und Farbe kreiert (Vec2)
b1 = Block(Vec2(10, 10), Vec2(0,26), brown)
b1_2 = Block(Vec2(10, 1), Vec2(0,25), green)
b2 = Block(Vec2(10, 20), Vec2(14,22), brown)
b2_2 = Block(Vec2(10, 1), Vec2(14,21), green)
b3 = Block(Vec2(5, 1), Vec2(28,19), brown)
b3_2 = Block(Vec2(5, 1), Vec2(28,18), green)
b4 = Block(Vec2(30, 20), Vec2(37,23), brown)
b4_2 = Block(Vec2(30, 1), Vec2(37,22), green)
b5 = Block(Vec2(6, 3), Vec2(44, 20), brown)
b5_2 = Block(Vec2(6, 1), Vec2(44, 19), green)

# Character wird initialisiert
tom = Character()


gegner = Gegner(Vec2(50,300),100, 600)

# Spielschleife
while True:
    # Screen wird bei jedem Schleifendurchlauf auf blaue Hintergrundfarbe resettet
    screen.fill((80,150,255))
    gegner.move()
    gegner.draw()


    # Blöcke und Character werden bei jedem Schleifendruchlauf geupdatet und gedrawt

    tom.draw()
    b1.update()
    b1_2.update()
    b2.update()
    b2_2.update()
    b3.update()
    b3_2.update()
    b4.update()
    b4_2.update()
    b5.update()
    b5_2.update()

    # Handles the shutting down of the programm, ignorieren!
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Keybinds für Bewegung des Characters nach links (A) und nach rechts (D) festgelegt
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]==False and keys[pygame.K_d]==False:
        tom.standstill()
    if keys[pygame.K_a]:
        tom.moveleft()
    if keys[pygame.K_d]:
        tom.moveright()


    dt = clock.get_time() / 1000.0 # Zeit seit dem letzten tick (Frame) in Sek.
    clock.tick(60) # Kontrolliert die Aktuallisierungen pro Minute (FPS)

    # Ruft update auf CollisionManager auf -> bewegt HitBoxen, prüft Kollisionen
    CollisionManager().update(dt)

    pygame.display.flip()
