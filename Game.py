from Menu import Menu
from DeathScreen import DeathScreen
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
            if self.state == GameState.MAIN_MENU:
                if not type(self.currentMenu) == Menu:
                    self.noMenu()
                    self.loadMainMenu()
                self.noLevel()
            if self.state == GameState.DEATH_SCREEN:
                if not type(self.currentMenu) == DeathScreen:
                    self.noMenu()
                    self.loadDeathScreen()
                self.noLevel()
            if self.state == GameState.GAME:
                if not type(self.currentLevel) == Level:
                    self.loadLevel()
                self.noMenu()
            if self.state == GameState.RESTART:
                self.noLevel()
                self.noMenu()
                self.state = GameState.GAME
            if self.state == GameState.NEXT_LEVEL:
                self.noLevel()
                self.noMenu()
                self.currentLevelIndex += 1
                self.state = GameState.GAME
            dt = self.update()
            self.draw()

    def noLevel(self):
        if self.currentLevel:
            self.currentLevel.remove()
            self.currentLevel = None

    def noMenu(self):
        if self.currentMenu:
            self.currentMenu = None

    def loadMainMenu(self):
        self.currentMenu = Menu()

    def loadDeathScreen(self):
        self.currentMenu = DeathScreen()

    def loadLevel(self):
        try:
            levelName = self.levelNameList[self.currentLevelIndex]
            self.currentLevel = Level.loadFile(levelName)
        except:
            print("No level on index " + str(self.currentLevelIndex))

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
