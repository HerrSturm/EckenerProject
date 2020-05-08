import pygame, sys
from GameState import GameState

class DeathScreen(object):
    def __init__(self, levelName):
        self.mainScreen = pygame.display.get_surface()
        self.levelName = levelName

    def draw(self):
        titleFont=pygame.font.SysFont('Arial Black',100)
        titleText= titleFont.render("GAME OVER", False, (255, 0 ,0))
        self.mainScreen.blit(titleText,(480,100))
        buttonFont=pygame.font.SysFont('Chandas', 30)
        pygame.draw.rect(self.mainScreen, (255, 255, 255), (480, 300, 400, 50))
        pygame.draw.rect(self.mainScreen, (255, 255, 255), (480, 400, 400, 50))
        pygame.draw.rect(self.mainScreen, (255, 255, 255), (480, 500, 400, 50))
        textButton1= buttonFont.render("Play " + self.levelName, False, (0, 0 ,0))
        textButton2= buttonFont.render("Options", False, (0, 0 ,0))
        textButton3= buttonFont.render("Quit Game", False, (0, 0 ,0))
        pygame.draw.rect(self.mainScreen, (255, 255, 255), (500, 300, 400, 50))
        pygame.draw.rect(self.mainScreen, (255, 255, 255), (500, 400, 400, 50))
        pygame.draw.rect(self.mainScreen, (255, 255, 255), (500, 500, 400, 50))
        self.mainScreen.blit(textButton1,(640, 315))
        self.mainScreen.blit(textButton2,(648, 415))
        self.mainScreen.blit(textButton3,(635, 515))

    def update(self, game):
        coordinates = 1
        pygame.event.get()
        keys = pygame.key.get_pressed()
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
