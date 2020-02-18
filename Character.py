import pygame
from HitBox import*
#CONST gravity
class Character():
    GRAVITY = 1
    JUMPVEL = 100
    MOVEVEL = 10
    def __init__(self, position): #Vec2 position
        self.isGrounded = False
        self.isGrounded_ = False
        size = Vec2(150,150)
        self.hitBox = HitBox(position, size, False, Layer("player"),Vec2(0,0))
        self.hitBox.onCollide(self.check_Grounded)
        CollisionManager().onBeforeUpdate(self.beforeCollisionManager)
        CollisionManager().onAfterUpdate(self.afterCollisionManager)
        self.mainScreen = pygame.display.get_surface()

    #checks if hitbox collided with ground
    def check_Grounded(self, other, dir):
        if dir == Direction.DOWN:
            self.isGrounded_ = True
    #draws the character on the screen
    def draw(self):
        pygame.draw.rect(self.mainScreen, (255, 255, 255), (self.hitBox.pos.values[0], self.hitBox.pos.values[1], self.hitBox.size.values[0], self.hitBox.size.values[1]))

    #updates the player
    def update(self, dt):
        self.draw()

    #gets called before the collisionmanager does stuff
    def beforeCollisionManager(dt):
        self.isGrounded_ = False
        self.vel += Vec2(0, -self.GRAVITY*dt)

    #gets called after the collisionmanager did stuff
    def afterCollisionManager(dt):
        #after col update
        self.isGrounded = self.isGrounded_

    def moveright(self):                           #Funktion um die Hitbox nach rechts zu bewegen (geschw. auf +1)
        self.hitBox.vel += Vec2(self.MOVEVEL,0)            #hitbox bewegt sich nach rechts

    def moveleft(self):                             #Funktion um die Hitbox nach links zu bewegen (geschw. auf -1)
        self.hitBox.vel += Vec2(-self.MOVEVEL,0)          #hitbox bewegt sich nach links

    def standstill(self):                           #Funktion um die Hitbox zum stehen zu bringen (geschw. auf 0)
        self.hitBox.vel.y = 0               #Hitbox bleibt stehen

    #makes the player jump:only when grounded
    def jump(self):
        if isGrounded:
            self.vel.y = 0
            self.vel += Vec2(0, self.JUMPVEL)
