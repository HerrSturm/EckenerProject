import pygame
from HitBox import*
from Direction import Direction
from sprites import runSprites
#CONST gravity
class Character():
    GRAVITY = 130
    JUMPVEL = 180
    MOVEVEL = 80
    def __init__(self, position): #Vec2 position
        self.hitBox = HitBox(Vec2(50,50), Vec2(125, 75), False, Layer("player"), Vec2(0.5, 0))
        self.mainScreen = pygame.display.get_surface()
        self.spriteCount = 2
        self.imageoriginal = pygame.image.load(runSprites(self.spriteCount)).convert_alpha()
        self.imagebig = pygame.transform.scale(self.imageoriginal, (125, 75))
        self.isGrounded = False
        self.isGrounded_ = False
        size = Vec2(40,58)
        self.hitBox = HitBox(position, size, False, Layer("player"),Vec2(0,0))
        self.hitBox.onCollide(self.check_Grounded)
        CollisionManager().onBeforeUpdate(self.beforeCollisionManager)
        CollisionManager().onAfterUpdate(self.afterCollisionManager)
        self.mainScreen = pygame.display.get_surface()

    #checks if hitbox collided with ground
    def check_Grounded(self, hitbox, other, dir):
        if dir == Direction.DOWN:
            self.isGrounded_ = True
    #draws the character on the screen
    def draw(self):
        self.imageoriginal = pygame.image.load(runSprites(self.spriteCount)).convert_alpha()
        self.imagebig = pygame.transform.scale(self.imageoriginal, (125, 75))
        pygame.draw.rect(self.mainScreen, (255, 255, 255), (self.hitBox.pos.values[0], self.hitBox.pos.values[1], self.hitBox.size.values[0], self.hitBox.size.values[1]))
        self.mainScreen.blit(self.imagebig, ((self.hitBox.pos.x)-43,(self.hitBox.pos.y)-15))
        self.spriteCount = self.spriteCount + 1
        print(self.spriteCount)
    #updates the player
    def update(self, dt):
        self.draw()

    #gets called before the collisionmanager does stuff
    def beforeCollisionManager(self, dt):
        self.isGrounded_ = False
        self.hitBox.vel += Vec2(0, self.GRAVITY*dt)

    #gets called after the collisionmanager did stuff
    def afterCollisionManager(self, dt):
        #after col update
        self.isGrounded = self.isGrounded_

    def moveright(self):                           #Funktion um die Hitbox nach rechts zu bewegen (geschw. auf +1)
        self.hitBox.vel.x = self.MOVEVEL            #hitbox bewegt sich nach rechts

    def moveleft(self):                             #Funktion um die Hitbox nach links zu bewegen (geschw. auf -1)
        self.hitBox.vel.x = -self.MOVEVEL          #hitbox bewegt sich nach links

    def standstill(self):                           #Funktion um die Hitbox zum stehen zu bringen (geschw. auf 0)
        self.hitBox.vel.x = 0               #Hitbox bleibt stehen

    #makes the player jump:only when grounded
    def jump(self):
        if self.isGrounded:
            self.hitBox.vel.y = 0
            self.hitBox.vel += Vec2(0, -self.JUMPVEL)
