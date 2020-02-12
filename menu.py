import pygame
pygame.init()
menuScreenSize = width, height = 1280, 720
menuScreen = pygame.display.set_mode(menuScreenSize)



def menu():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
            sys.exit()

def update():
    global menuScreen
    global menuScreenSize
    pygame.draw.rect(menuScreen, (255, 255, 255), (10, 20, menuScreenSize[0], menuScreenSize[1]))

i= True

while i==True:
    menu()
    print(1)
    update()
