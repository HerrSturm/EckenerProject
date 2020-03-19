import pygame, sys
pygame.init()
class Options(object):
    def __init__(self):
        self.mainScreen = pygame.display.get_surface()
        pygame.draw.rect(self.mainScreen, (255, 255, 255), (440, 300, 400, 50))
        pygame.draw.rect(self.mainScreen, (255, 255, 255), (440, 400, 400, 50))
        pygame.draw.rect(self.mainScreen, (255, 255, 255), (440, 500, 400, 50))
    def draw(self):
        titleFont=pygame.font.SysFont('Arial Black',70)
        buttonFont=pygame.font.SysFont('Chandas', 30)
        titleText= titleFont.render("Options", False, (255, 255 ,255))
        textButton1= buttonFont.render("Play", False, (0, 0 ,0))
        textButton2= buttonFont.render("Options", False, (0, 0 ,0))
        textButton3= buttonFont.render("Quit Game", False, (0, 0 ,0))
        self.mainScreen.blit(titleText,(450,100))
        self.mainScreen.blit(textButton1,(595, 290))
        self.mainScreen.blit(textButton2,(580, 390))
        self.mainScreen.blit(textButton3,(560, 490))
        pygame.display.flip()

    def update(self):
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
