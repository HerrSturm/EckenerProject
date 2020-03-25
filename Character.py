import pygame
from HitBox import*
from Direction import Direction
from sprites import runSprites, fallSprites, idleSprites, wallSlideSprites, saltoSprites, crouchSprites, attackSprites
#CONST gravity
class Character():
    GRAVITY = 300
    JUMPVEL = 275
    MOVEVEL = 200
    def __init__(self, position): #Vec2 position
        self.heading = 1
        self.spriteCount = 2
        self.imageoriginal = runSprites(self.spriteCount)
        self.imagebig = pygame.transform.scale(self.imageoriginal, (125, 75))
        self.isGrounded = False
        self.isGrounded_ = False
        self.isCrouching = False
        self.health = 1
        self.isSliding = False
        self.lives = 3
        self.protection = 3 #in sekunden nach Lebensverlust angegeben
        self.heartImage = pygame.image.load('Graphics/GUI/heart.png')
        self.lvlUp = False
        self.hitBox = HitBox(position * 24, Vec2(40,58), False, Layer("player"),Vec2(0.5,0))
        self.hitBox.onCollide(self.check_Grounded)
        self.hitBox.onCollide(self.hurt, Layer("deadly"))
        self.hitBox.onCollide(self.end, Layer("end"))
        CollisionManager().onBeforeUpdate(self.beforeCollisionManager)
        CollisionManager().onAfterUpdate(self.afterCollisionManager)


    #checks if hitbox collided with ground
    def check_Grounded(self, hitbox, other, dir, layer):
        if dir == Direction.DOWN:
            self.isGrounded_ = True
    #draws the character on the screen
    def draw(self, surface):
        keys = pygame.key.get_pressed()
        self.isSliding = False
        #checks if the "s" button is pressed and the character is therefore "crouching"

        if self.isCrouching:
            self.hitBox.size.y = 38
        else:
            self.hitBox.size.y = 58
        pygame.draw.rect(surface, (0, 0, 0), (self.hitBox.pos.values[0], self.hitBox.pos.values[1], self.hitBox.size.values[0], self.hitBox.size.values[1]))
        if self.isGrounded == True and self.hitBox.vel.x == 0 and self.isCrouching:
            self.imageoriginal = crouchSprites(self.spriteCount)
            self.imagebig = pygame.transform.scale(self.imageoriginal, (125, 75))
        elif self.isGrounded == True and self.hitBox.vel.x == 0:
            self.imageoriginal = idleSprites(self.spriteCount)
            self.imagebig = pygame.transform.scale(self.imageoriginal, (125, 75))
        elif self.isGrounded == False and self.hitBox.vel.x == 0 and self.hitBox.vel.y >= 0 and keys[pygame.K_a]:
            self.imageoriginal = wallSlideSprites(self.spriteCount)
            self.imagebig = pygame.transform.scale(self.imageoriginal, (125, 75))
            self.isSliding = True
        elif self.isGrounded == False and self.hitBox.vel.x == 0 and self.hitBox.vel.y >= 0 and keys[pygame.K_d]:
            self.imageoriginal = wallSlideSprites(self.spriteCount)
            self.imagebig = pygame.transform.scale(self.imageoriginal, (125, 75))
            self.isSliding = True
        elif self.isGrounded == True and self.isCrouching:
            self.imageoriginal = crouchSprites(self.spriteCount)
            self.imagebig = pygame.transform.scale(self.imageoriginal, (125, 75))
        elif self.isGrounded == True:
            self.imageoriginal = runSprites(self.spriteCount)
            self.imagebig = pygame.transform.scale(self.imageoriginal, (125, 75))
        elif self.isGrounded == False and self.hitBox.vel.y <= -20:
            self.imageoriginal = pygame.image.load("Graphics/aAllGraphics/Adventurer/adventurer-jump-02.png").convert_alpha()
            self.imagebig = pygame.transform.scale(self.imageoriginal, (125, 75))
        elif self.isGrounded == False and self.hitBox.vel.y > -20 and self.hitBox.vel.y <= 20:
            self.imageoriginal = pygame.image.load("Graphics/aAllGraphics/Adventurer/adventurer-jump-03.png").convert_alpha()
            self.imagebig = pygame.transform.scale(self.imageoriginal, (125, 75))
        elif self.isGrounded == False:
            self.imageoriginal = fallSprites(self.spriteCount)
            self.imagebig = pygame.transform.scale(self.imageoriginal, (125, 75))

        """Ausrichtung bestimmen und ggf. Bild drehen"""
        if self.hitBox.vel.x > 0:
            self.heading = 1
        elif self.hitBox.vel.x < 0:
            self.heading = -1
        if self.heading == -1:
            self.imagebig = pygame.transform.flip(self.imagebig,True,False)
        if self.isSliding and keys[pygame.K_a]:
            surface.blit(self.imagebig, ((self.hitBox.pos.x)-45,(self.hitBox.pos.y)-15))
        elif self.isSliding and keys[pygame.K_d]:
            surface.blit(self.imagebig, ((self.hitBox.pos.x)-40,(self.hitBox.pos.y)-15))
        elif self.isCrouching:
            self.hitBox.pos.y = self.hitBox.pos.y + 20
            surface.blit(self.imagebig, ((self.hitBox.pos.x)-45,(self.hitBox.pos.y)-55))
        else:
            surface.blit(self.imagebig, ((self.hitBox.pos.x)-50,(self.hitBox.pos.y)-15))
        self.spriteCount = self.spriteCount + 1
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
        if keys[pygame.K_s]:
            self.GRAVITY = 1200
            if self.isGrounded:
                self.isCrouching = True
            else:
                self.isCrouching = False
        else:
            self.GRAVITY = 300



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

    def moveright(self):
        #Funktion um die Hitbox nach rechts zu bewegen (geschw. auf +1)
        if self.isCrouching == False:
            self.hitBox.vel.x = self.MOVEVEL
        else:
            self.hitBox.vel.x = self.MOVEVEL/2
        #hitbox bewegt sich nach rechts

    def moveleft(self):
        #Funktion um die Hitbox nach links zu bewegen (geschw. auf -1)
        if self.isCrouching == False:
            self.hitBox.vel.x = -self.MOVEVEL
        else:
            self.hitBox.vel.x = -self.MOVEVEL/2
        #hitbox bewegt sich nach links

    def standstill(self):
        #Funktion um die Hitbox zum stehen zu bringen (geschw. auf 0)
        self.hitBox.vel.x = 0
        #Hitbox bleibt stehen

    #makes the player jump:only when grounded
    def jump(self):
        if self.isGrounded :
            self.hitBox.vel.y = 0
            self.hitBox.vel += Vec2(0, -self.JUMPVEL)

#010B1TC01N1000CYB3R110H4CK101
    #check enemy hurts me?
    def hurt(self, hitbox, other, dir, layer):
        if self.protection <= 0:
            self.lives -= 1
            self.protection = 3
            print("AUA")

    def protectionCorrection(self, dt):
        self.protection -= dt

    def end(self, hitbox, other, dir, layer):
        print('Level beendet!')
        self.lvlUp = True
