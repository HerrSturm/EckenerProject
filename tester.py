import sys, pygame, time
from Block import Block
pygame.init()

brown = (150,80,50)
blue = (80,150,255)
green = (50,100,50)


size = width, heigth = 1400, 800
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.flip()

screen.fill((80,150,255))

b1 = Block((10, 10), (0,26), brown)
b2 = Block((10, 1), (0,25), green)
b3 = Block((10, 20), (14,20), brown)
b4 = Block((10, 1), (14,19), green)
b5 = Block((5, 1), (30,19), brown)
b6 = Block((5, 1), (30,18), green)
b7 = Block((30, 20), (37,23), brown)
b8 = Block((30, 1), (37,22), green)



while True:

    screen.fill((80,150,255))
    Block.move(b1,(1,-1))
    Block.update(b2)
    Block.update(b3)
    Block.update(b4)
    Block.update(b5)
    Block.update(b6)
    Block.update(b7)
    Block.update(b8)
    #handles the shutting down of the programm, ignorieren!
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()



    clock.tick(60) # Kontrolliert die Aktuallisierungen pro Minute (FPS)


    pygame.display.flip()
