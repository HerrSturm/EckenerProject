import pygame, sys
from GameState import GameState

class Menu(object):
    def __init__(self, levelName):
        self.mainScreen = pygame.display.get_surface()
        self.levelName = levelName

    def draw(self):
        titleFont=pygame.font.SysFont('Arial Black',70)
        buttonFont=pygame.font.SysFont('Chandas', 30)
        titleText= titleFont.render("Ihre Werbung hier", False, (255, 255 ,255))
        textButton1= buttonFont.render("Play " + self.levelName, False, (0, 0 ,0))
        textButton2= buttonFont.render("Options", False, (0, 0 ,0))
        textButton3= buttonFont.render("Quit Game", False, (0, 0 ,0))
        self.mainScreen.blit(titleText,(500,100))
        pygame.draw.rect(self.mainScreen, (255, 255, 255), (440, 300, 400, 50))
        pygame.draw.rect(self.mainScreen, (255, 255, 255), (440, 400, 400, 50))
        pygame.draw.rect(self.mainScreen, (255, 255, 255), (440, 500, 400, 50))
        self.mainScreen.blit(textButton1,(595, 320))
        self.mainScreen.blit(textButton2,(580, 420))
        self.mainScreen.blit(textButton3,(560, 520))

    def update(self, game):
        pygame.display.flip()
        coordinates = 1
        keys = pygame.key.get_pressed()
        pygame.event.get()
        lMouse=pygame.mouse.get_pressed()[0]
        pygame.mouse.get_pos()[coordinates]
        if 440 <= pygame.mouse.get_pos()[0] and pygame.mouse.get_pos()[0] <= 840 and 300 <= pygame.mouse.get_pos()[1] and 350 >= pygame.mouse.get_pos()[1]:
            if lMouse:
                game.state = GameState.GAME
        if keys[pygame.K_SPACE]:
                game.state = GameState.GAME
        if 440 <= pygame.mouse.get_pos()[0] and pygame.mouse.get_pos()[0] <= 840 and 400 <= pygame.mouse.get_pos()[1] and 450 >= pygame.mouse.get_pos()[1]:
            if lMouse:
                game.state = GameState.OPTIONS
        if 440 <= pygame.mouse.get_pos()[0] and pygame.mouse.get_pos()[0] <= 840 and 500 <= pygame.mouse.get_pos()[1] and 550 >= pygame.mouse.get_pos()[1]:
            if lMouse:
                sys.exit()
