import sys, pygame, time
from Block import Block
from Vec2 import Vec2
from Character import Character
from CollisionManager import CollisionManager
from GegnerClass import *
from Level import *
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

level = Level.loadFile("level02.json")

# Spielschleife
while True:
    # Screen wird bei jedem Schleifendurchlauf auf blaue Hintergrundfarbe resettet
    screen.fill((80,150,255))


    # Handles the shutting down of the programm, ignorieren!
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    dt = clock.get_time() / 1000.0 # Zeit seit dem letzten tick (Frame) in Sek.
    clock.tick(60) # Kontrolliert die Aktuallisierungen pro Minute (FPS)

    # Ruft update auf CollisionManager auf -> bewegt HitBoxen, prüft Kollisionen
    level.update(dt)
    level.draw()

    pygame.display.flip()
