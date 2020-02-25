import pygame
from HitBox import*
class Character():
    def __init__(self):
        self.image = pygame.image.load("Graphics/aAllGraphics/Adventurer/adventurer-idle-00.png").convert_alpha()
        self.imagebig = pygame.transform.scale(self.image, (125, 75))
        #self.run = ["adventurer-run-00.png","adventurer-run-01.png","adventurer-run-02.png",
                #"adventurer-run-03.png","adventurer-run-04.png","adventurer-run-05.png"]
        self.hitBox = HitBox(Vec2(50,50), Vec2(125, 75), False, Layer("player"), Vec2(0.5, 0))
        self.mainScreen = pygame.display.get_surface()
        #pygame.draw.rect(self.mainScreen, (255, 255, 255), (self.hitBox.pos.values[0], self.hitBox.pos.values[1], self.hitBox.size.values[0], self.hitBox.size.values[1]))
    def draw(self):
        self.mainScreen.blit(self.imagebig, (self.hitBox.pos.x,self.hitBox.pos.y))
        #pygame.draw.rect(self.mainScreen, (255, 255, 255), (self.hitBox.pos.values[0], self.hitBox.pos.values[1], self.hitBox.size.values[0], self.hitBox.size.values[1]))
    def moveright(self):                           #Funktion um die Hitbox nach rechts zu bewegen (geschw. auf +1)
        self.hitBox.vel = Vec2(300,0)            #hitbox bewegt sich nach rechts

    def moveleft(self):                             #Funktion um die Hitbox nach links zu bewegen (geschw. auf -1)
        self.hitBox.vel = Vec2(-300,0)          #hitbox bewegt sich nach links

    def standstill(self):                           #Funktion um die Hitbox zum stehen zu bringen (geschw. auf 0)
        self.hitBox.vel = Vec2(0,0)               #Hitbox bleibt stehen
