from enum import Enum

class GameState(Enum):
    MAIN_MENU = 0
    DEATH_SCREEN = 1
    OPTIONS = 2
    GAME = 3
    RESTART = 4
    NEXT_LEVEL = 5
