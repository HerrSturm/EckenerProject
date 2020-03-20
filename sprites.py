#Hier befinden sich alle Sprites, die in der Animation verwendet werden sollen.
import pygame
path = "Graphics/aAllGraphics/Adventurer/"
def runSprites(x):
    SpritesRun = [pygame.image.load(path+"adventurer-run-00.png").convert_alpha(),
                    pygame.image.load(path+"adventurer-run-01.png").convert_alpha(),
                    pygame.image.load(path+"adventurer-run-02.png").convert_alpha(),
                    pygame.image.load(path+"adventurer-run-03.png").convert_alpha(),
                    pygame.image.load(path+"adventurer-run-04.png").convert_alpha(),
                    pygame.image.load(path+"adventurer-run-05.png").convert_alpha()]
    return(SpritesRun[x//4%len(SpritesRun)-1])
def fallSprites(x):
    SpritesFall = [pygame.image.load(path+"adventurer-fall-00.png").convert_alpha(),
                    pygame.image.load(path+"adventurer-fall-01.png").convert_alpha()]
    return(SpritesFall[x//10%len(SpritesFall)-1])
def idleSprites(x):
    SpritesIdle = [pygame.image.load(path+"adventurer-idle-00.png").convert_alpha(),
                    pygame.image.load(path+"adventurer-idle-01.png").convert_alpha(),
                    pygame.image.load(path+"adventurer-idle-02.png").convert_alpha()]
    return(SpritesIdle[x//15%len(SpritesIdle)-1])
def wallSlideSprites(x):
    WallSlide = [pygame.image.load(path+"WallSlide0.png").convert_alpha(),
                pygame.image.load(path+"WallSlide1.png").convert_alpha()]
    return(WallSlide[x//10%len(WallSlide)-1])
#pygame.image.load(idleSprites(self.spriteCount)).convert_alpha()
def saltoSprites(x):
    SaltoSprites = [pygame.image.load(path+"adventurer-smrslt-00.png").convert_alpha(),
                    pygame.image.load(path+"adventurer-smrslt-01.png").convert_alpha(),
                    pygame.image.load(path+"adventurer-smrslt-02.png").convert_alpha(),
                    pygame.image.load(path+"adventurer-smrslt-03.png").convert_alpha()]
    return(SaltoSprites[x//6%len(SaltoSprites)-1])
def crouchSprites(x):
    CrouchSprites = [pygame.image.load(path+"adventurer-crouch-00.png").convert_alpha(),
                    pygame.image.load(path+"adventurer-crouch-01.png").convert_alpha(),
                    pygame.image.load(path+"adventurer-crouch-02.png").convert_alpha(),
                    pygame.image.load(path+"adventurer-crouch-03.png").convert_alpha()]
    return(CrouchSprites[x//14%len(CrouchSprites)-1])
def attackSprites(x):
    AttackSprites = [pygame.image.load(path+"adventurer-attack2-00.png").convert_alpha(),
                    pygame.image.load(path+"adventurer-attack2-01.png").convert_alpha(),
                    pygame.image.load(path+"adventurer-attack2-02.png").convert_alpha(),
                    pygame.image.load(path+"adventurer-attack2-03.png").convert_alpha(),
                    pygame.image.load(path+"adventurer-attack2-04.png").convert_alpha()]
    return(AttackSprites[4-round(x/20)])
