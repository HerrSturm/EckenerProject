#Hier befinden sich alle Sprites, die in der Animation verwendet werden sollen.
import pygame
path = "Graphics/aAllGraphics/Adventurer/"

characterScale = (125,75)

RUNSPRITES =   [pygame.transform.scale(pygame.image.load(path+"adventurer-run-00.png"), characterScale),
                pygame.transform.scale(pygame.image.load(path+"adventurer-run-01.png"), characterScale),
                pygame.transform.scale(pygame.image.load(path+"adventurer-run-02.png"), characterScale),
                pygame.transform.scale(pygame.image.load(path+"adventurer-run-03.png"), characterScale),
                pygame.transform.scale(pygame.image.load(path+"adventurer-run-04.png"), characterScale),
                pygame.transform.scale(pygame.image.load(path+"adventurer-run-05.png"), characterScale)]

FALLSPRITES = [pygame.transform.scale(pygame.image.load(path+"adventurer-fall-00.png"), characterScale),
                pygame.transform.scale(pygame.image.load(path+"adventurer-fall-01.png"), characterScale)]

IDLESPRITES = [pygame.transform.scale(pygame.image.load(path+"adventurer-idle-00.png"), characterScale),
                pygame.transform.scale(pygame.image.load(path+"adventurer-idle-01.png"), characterScale),
                pygame.transform.scale(pygame.image.load(path+"adventurer-idle-02.png"), characterScale)]

WALLSLIDE_SPRITES = [pygame.transform.scale(pygame.image.load(path+"WallSlide0.png"), characterScale),
                    pygame.transform.scale(pygame.image.load(path+"WallSlide1.png"), characterScale)]

SALTOSPRITES = [pygame.transform.scale(pygame.image.load(path+"adventurer-smrslt-00.png"), characterScale),
                pygame.transform.scale(pygame.image.load(path+"adventurer-smrslt-01.png"), characterScale),
                pygame.transform.scale(pygame.image.load(path+"adventurer-smrslt-02.png"), characterScale),
                pygame.transform.scale(pygame.image.load(path+"adventurer-smrslt-03.png"), characterScale)]

CROUCHSPRITES = [pygame.transform.scale(pygame.image.load(path+"adventurer-crouch-00.png"), characterScale),
                pygame.transform.scale(pygame.image.load(path+"adventurer-crouch-01.png"), characterScale),
                pygame.transform.scale(pygame.image.load(path+"adventurer-crouch-02.png"), characterScale),
                pygame.transform.scale(pygame.image.load(path+"adventurer-crouch-03.png"), characterScale)]

ATTACKSPRITES = [pygame.transform.scale(pygame.image.load(path+"adventurer-attack2-00.png"), characterScale),
                pygame.transform.scale(pygame.image.load(path+"adventurer-attack2-01.png"), characterScale),
                pygame.transform.scale(pygame.image.load(path+"adventurer-attack2-02.png"), characterScale),
                pygame.transform.scale(pygame.image.load(path+"adventurer-attack2-03.png"), characterScale),
                pygame.transform.scale(pygame.image.load(path+"adventurer-attack2-04.png"), characterScale)]

JUMPSPRITES = [pygame.transform.scale(pygame.image.load(path+"adventurer-jump-02.png"), characterScale),
                pygame.transform.scale(pygame.image.load(path+"adventurer-jump-03.png"), characterScale)]

def runSprites(x):
    global RUNSPRITES
    return(RUNSPRITES[x//4%len(RUNSPRITES)-1].convert_alpha())


def fallSprites(x):
    global FALLSPRITES
    return(FALLSPRITES[x//10%len(FALLSPRITES)-1].convert_alpha())


def idleSprites(x):
    global IDLESPRITES
    return(IDLESPRITES[x//15%len(IDLESPRITES)-1].convert_alpha())

def wallSlideSprites(x):
    global WALLSLIDE_SPRITES
    return(WALLSLIDE_SPRITES[x//10%len(WALLSLIDE_SPRITES)-1].convert_alpha())

def saltoSprites(x):
    global SALTOSPRITES
    return(SALTOSPRITES[x//6%len(SALTOSPRITES)-1].convert_alpha())

def crouchSprites(x):
    global CROUCHSPRITES
    return(CROUCHSPRITES[x//14%len(CROUCHSPRITES)-1].convert_alpha())

def attackSprites(x):
    global ATTACKSPRITES
    return(ATTACKSPRITES[4-round(x/20)].convert_alpha())

def jumpSprites(x):
    global JUMPSPRITES
    return JUMPSPRITES[x].convert_alpha()
