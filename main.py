import sys, pygame
pygame.init()
mainScreenSize = width, height = 1280, 720
mainScreen = pygame.display.set_mode(mainScreenSize)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    pygame.display.flip()
    #Shutdownhandling
    if keys[pygame.K_ESCAPE]:
        sys.exit()
