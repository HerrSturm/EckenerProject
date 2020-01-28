import sys, pygame, blockClass, time
pygame.init()

brown = (150,80,50)
blue = (80,150,255)
green = (50,100,50)


size = width, heigth = 1400, 800
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.flip()

screen.fill((80,150,255))

while True:
    #handles the shutting down of the programm, ignorieren!
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    b1 = blockClass.block((10, 10), (0,26), brown)
    b2 = blockClass.block((10, 1), (0,25), green)
    b3 = blockClass.block((10, 20), (14,20), brown)
    b4 = blockClass.block((10, 1), (14,19), green)
    b5 = blockClass.block((5, 1), (30,19), brown)
    b6 = blockClass.block((5, 1), (30,18), green)
    b7 = blockClass.block((30, 20), (37,23), brown)
    b8 = blockClass.block((30, 1), (37,22), green)

    clock.tick(60) # Kontrolliert die Aktuallisierungen pro Minute (FPS)


    pygame.display.flip()
