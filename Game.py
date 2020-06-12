import sys
from Menu import Menu
from DeathScreen import DeathScreen
from Options import Options
from Level import Level
from enum import Enum
from GameState import GameState
import pygame

class Game:

    def __init__(self, levelNameList):
        self.levelNameList = levelNameList
        self.currentLevelIndex = 0
        self.currentLevel = None
        self.currentMenu = None
        self.state = GameState.MAIN_MENU
        self.clock = pygame.time.Clock()
        self.init()
        self.loop()

    def init(self):
        size = (1400, 800)
        pygame.display.set_mode(size)
        self.screen = pygame.display.get_surface()

    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            needStateUpdate = True
            while needStateUpdate:
                needStateUpdate = False
                if self.state == GameState.MAIN_MENU:
                    self.noLevel()
                    if type(self.currentMenu) != Menu:
                        self.noMenu()
                        self.loadMainMenu()
                if self.state == GameState.DEATH_SCREEN:
                    self.noLevel()
                    if type(self.currentMenu) != DeathScreen:
                        self.noMenu()
                        self.loadDeathScreen()
                if self.state == GameState.OPTIONS:
                    self.noLevel()
                    if type(self.currentMenu) != Options:
                        self.noMenu()
                        self.loadOptions()
                if self.state == GameState.GAME:
                    self.noMenu()
                    if type(self.currentLevel) != Level:
                        if not self.loadLevel():
                            self.state = GameState.MAIN_MENU
                            needStateUpdate = True
                if self.state == GameState.RESTART:
                    self.noLevel()
                    self.noMenu()
                    self.state = GameState.DEATH_SCREEN
                    needStateUpdate = True
                if self.state == GameState.NEXT_LEVEL:
                    self.noLevel()
                    self.noMenu()
                    self.currentLevelIndex += 1
                    self.state = GameState.MAIN_MENU
                    needStateUpdate = True

            dt = self.update()
            self.draw()

    def noLevel(self):
        if self.currentLevel:
            self.currentLevel.remove()
            self.currentLevel = None

    def noMenu(self):
        if self.currentMenu:
            self.currentMenu = None

    def getCurrentLevelName(self):
        if self.currentLevelIndex >= len(self.levelNameList):
            return "no level :D"
        return "level " + str(self.currentLevelIndex + 1)

    def loadMainMenu(self):
        self.currentMenu = Menu(self.getCurrentLevelName())

    def loadDeathScreen(self):
        self.currentMenu = DeathScreen(self.getCurrentLevelName())

    def loadOptions(self):
        self.currentMenu = Options()

    def loadLevel(self):
        if self.currentLevelIndex >= len(self.levelNameList):
            return False
        try:
            levelName = self.levelNameList[self.currentLevelIndex]
            self.currentLevel = Level.loadFile(levelName)
            return True
        except Exception as e:
            print("No level on index " + str(self.currentLevelIndex), e)
        return False

    def draw(self):
        self.screen.fill((0, 0, 0))
        if self.currentLevel:
            self.currentLevel.draw()
        if self.currentMenu:
            self.currentMenu.draw()
        pygame.display.flip()

    def update(self):
        dt = self.clock.get_time() / 1000.0 # Zeit seit dem letzten tick (Frame) in Sek.
        self.clock.tick(60) # Kontrolliert die Aktuallisierungen pro Minute (FPS)
        if self.currentLevel:
            self.currentLevel.update(self, dt)
        if self.currentMenu:
            self.currentMenu.update(self)
        return dt
