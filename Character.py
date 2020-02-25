import pygame
from HitBox import*
from Direction import Direction
#CONST gravity
class Character():
    GRAVITY = 130
    JUMPVEL = 180
    MOVEVEL = 80
    def __init__(self, position): #Vec2 position
        self.isGrounded = False
        self.isGrounded_ = False
        size = Vec2(40,75)
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
    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), (self.hitBox.pos.values[0], self.hitBox.pos.values[1], self.hitBox.size.values[0], self.hitBox.size.values[1]))

    #updates the player
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]==False and keys[pygame.K_d]==False:
            self.standstill()
        if keys[pygame.K_a]:
            self.moveleft()
        if keys[pygame.K_d]:
            self.moveright()
        if keys[pygame.K_w]:
            self.jump()

    def remove(self):
        self.hitBox.remove()

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
