import pygame, sys
pygame.init()

class Death(object):
    def __init__(self):
        self.mainScreen = pygame.display.get_surface()

    def draw(self):
        titleFont=pygame.font.SysFont('Arial Black',100)
        titleText= titleFont.render("GAME OVER", False, (255, 0 ,0))
        self.mainScreen.blit(titleText,(350,100))
        buttonFont=pygame.font.SysFont('Chandas', 30)
        pygame.display.flip()
        pygame.draw.rect(self.mainScreen, (255, 255, 255), (470, 300, 400, 50))
        pygame.draw.rect(self.mainScreen, (255, 255, 255), (470, 400, 400, 50))
        pygame.draw.rect(self.mainScreen, (255, 255, 255), (470, 500, 400, 50))
        textButton1= buttonFont.render("Play", False, (0, 0 ,0))
        textButton2= buttonFont.render("Options", False, (0, 0 ,0))
        textButton3= buttonFont.render("Quit Game", False, (0, 0 ,0))
        pygame.draw.rect(self.mainScreen, (255, 255, 255), (440, 300, 400, 50))
        pygame.draw.rect(self.mainScreen, (255, 255, 255), (440, 400, 400, 50))
        pygame.draw.rect(self.mainScreen, (255, 255, 255), (440, 500, 400, 50))
        self.mainScreen.blit(textButton1,(610, 290))
        self.mainScreen.blit(textButton2,(590, 390))
        self.mainScreen.blit(textButton3,(570, 490))
    def update(self):
        while True:
            pygame.display.flip()
            coordinates = 1
            pygame.event.get()
            lMouse=pygame.mouse.get_pressed()[0]
            pygame.mouse.get_pos()[coordinates]
            if 440 <= pygame.mouse.get_pos()[0] and pygame.mouse.get_pos()[0] <= 840 and 300 <= pygame.mouse.get_pos()[1] and 350 >= pygame.mouse.get_pos()[1]:
                if lMouse:
                    pass
            if 440 <= pygame.mouse.get_pos()[0] and pygame.mouse.get_pos()[0] <= 840 and 400 <= pygame.mouse.get_pos()[1] and 450 >= pygame.mouse.get_pos()[1]:
                if lMouse:
                    pass
            if 440 <= pygame.mouse.get_pos()[0] and pygame.mouse.get_pos()[0] <= 840 and 500 <= pygame.mouse.get_pos()[1] and 550 >= pygame.mouse.get_pos()[1]:

                if lMouse:
                    sys.exit()

mainScreenSize = width, heigth = 1400, 800
mainScreen = pygame.display.set_mode(mainScreenSize)
death=Death()
death.draw()
death.update()
keys = pygame.key.get_pressed()
if keys[pygame.K_ESCAPE]:
    #menu.menu()
    sys.exit()
