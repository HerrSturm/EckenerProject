import sys, pygame, characterClass, menu
pygame.init()
mainScreenSize = width, height = 1280, 720
mainScreen = pygame.display.set_mode(mainScreenSize)
character=characterClass.Character()

class State(Enum):
    MAIN_MENU = 0
    GAME = 1

state = State.MAIN_MENU

while True:
    if state == State.MAIN_MENU:
        state = State.GAME
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    pygame.display.flip()
    #Shutdownhandling
    menu.pause
    if keys[pygame.K_ESCAPE]:
        #menu.menu()
        sys.exit()
    mainScreen.fill((0,0,0))
    character.update()
