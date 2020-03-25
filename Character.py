import pygame
from HitBox import*
from Direction import Direction
from GameState import GameState
from sprites import runSprites, fallSprites, idleSprites, wallSlideSprites, saltoSprites, crouchSprites, attackSprites, jumpSprites
#CONST gravity
class Character():
    GRAVITY = 300
    JUMPVEL = 275
    MOVEVEL = 200
    def __init__(self, position): #Vec2 position
        self.heading = 1
        self.spriteCount = 2
        self.image = runSprites(self.spriteCount)
        self.isGrounded = False
        self.isGrounded_ = False
        self.isCrouching = False
        self.toggleCrouching = False
        self.health = 1
        self.isMoving = True
        self.isSliding = False
        self.lives = 3
        self.protection = 3 #in sekunden nach Lebensverlust angegeben
        self.heartImage = pygame.image.load('Graphics/GUI/heart.png')
        self.lvlUp = False
        self.hitBox = HitBox(position, Vec2(40,58), False, Layer("player"),Vec2(0.5,0))
        self.hitBox.onCollide(self.check_Grounded)
        self.hitBox.onCollide(self.hurt, Layer("deadly"))
        self.hitBox.onCollide(self.end, Layer("end"))
        CollisionManager().onBeforeUpdate(self.beforeCollisionManager)
        CollisionManager().onAfterUpdate(self.afterCollisionManager)
        self.movingSolid = 0

    #checks if hitbox collided with ground
    def check_Grounded(self, hitbox, other, dir, layer):
        if dir == Direction.DOWN:
            self.isGrounded_ = True
            if other.vel.x != 0:
                self.hitBox.vel.x = other.vel.x
                self.movingSolid = other.vel.x
        else:
            isGrounded = False
    #draws the character on the screen
    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), (self.hitBox.pos.values[0], self.hitBox.pos.values[1], self.hitBox.size.values[0], self.hitBox.size.values[1]))

        self.isSliding = False

        """Handling of Hitbox change, when status changes from to crouching"""
        if self.isCrouching and not(self.toggleCrouching):
            self.toggleCrouching = True
            self.hitBox.size.y = 38
            self.hitBox.pos.y += 20
        elif not(self.isCrouching) and self.toggleCrouching:
            self.hitBox.size.y = 58
            self.hitBox.pos.y -= 20
            self.toggleCrouching = False

        if self.isGrounded == True and self.hitBox.vel.x == 0 and self.isCrouching:
            self.image = crouchSprites(self.spriteCount)
        elif self.isGrounded == True and self.hitBox.vel.x == 0:
            self.image = idleSprites(self.spriteCount)
        elif self.isGrounded == False and self.hitBox.vel.x == 0 and self.hitBox.vel.y >= 0 and self.isMoving:
            self.image = wallSlideSprites(self.spriteCount)
            self.isSliding = True
        elif self.isGrounded == False and self.hitBox.vel.x == 0 and self.hitBox.vel.y >= 0 and self.isMoving:
            self.image = wallSlideSprites(self.spriteCount)
            self.isSliding = True
        elif self.isGrounded == True and self.isCrouching:
            self.image = crouchSprites(self.spriteCount)
        elif self.isGrounded == True:
            if self.hitBox.vel.x == self.movingSolid and not self.updateKeys():
                self.image = idleSprites(self.spriteCount)
            else:
                self.image = runSprites(self.spriteCount)
        elif self.isGrounded == True and self.isCrouching:
            self.image = crouchSprites(self.spriteCount)
        elif self.isGrounded == False and self.hitBox.vel.y <= -20:
            self.image = jumpSprites(0)
        elif self.isGrounded == False and self.hitBox.vel.y > -20 and self.hitBox.vel.y <= 20:
            self.image = jumpSprites(1)
        elif self.isGrounded == False:
            self.image = fallSprites(self.spriteCount)

        if self.heading == -1:
            self.image = pygame.transform.flip(self.image,True,False)

        if self.isSliding and self.isMoving:
            surface.blit(self.image, ((self.hitBox.pos.x)-45,(self.hitBox.pos.y)-15))
        elif self.isSliding and keys[pygame.K_d]:
            surface.blit(self.image, ((self.hitBox.pos.x)-40,(self.hitBox.pos.y)-15))
        elif self.isCrouching:
            surface.blit(self.image, ((self.hitBox.pos.x)-45,(self.hitBox.pos.y)-35))
        else:
            surface.blit(self.image, ((self.hitBox.pos.x)-50,(self.hitBox.pos.y)-15))
        self.spriteCount = self.spriteCount + 1
    #updates the player

    def setHeading(self):
        if self.hitBox.vel.x > 0 and not self.hitBox.vel.x == self.movingSolid:
            self.heading = 1
        elif self.hitBox.vel.x < 0 and not self.hitBox.vel.x == self.movingSolid:
            self.heading = -1

    def update(self, game, dt):
        self.setHeading()
        self.protectionCorrection(dt)
        self.updateKeys()
        if self.lives <= 0:
            game.state = GameState.RESTART
        if self.lvlUp:
            game.state = GameState.NEXT_LEVEL

    def remove(self):
        self.hitBox.remove()

    #gets called before the collisionmanager does stuff
    def beforeCollisionManager(self, dt):
        self.isGrounded_ = False
        self.hitBox.vel += Vec2(0, self.GRAVITY*dt)
        self.movingSolid = 0

    #gets called after the collisionmanager did stuff
    def afterCollisionManager(self, dt):
        #after col update
        self.isGrounded = self.isGrounded_

    def updateKeys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.moveleft()
            self.isMoving = True
        if keys[pygame.K_d]:
            self.moveright()
            self.isMoving = True
        if keys[pygame.K_w]:
            self.jump()
        if keys[pygame.K_s]:
            self.GRAVITY = 1200
            if self.isGrounded:
                self.isCrouching = True
            else:
                self.isCrouching = False
        else:
            self.isCrouching = False
            self.GRAVITY = 300

        if keys[pygame.K_a]==False and keys[pygame.K_d]==False:
            self.standstill()
            self.isMoving = False
            if not keys[pygame.K_w]:
                return False
        else:
            return True


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
        self.hitBox.vel.x = self.movingSolid
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
            self.loseLife()

    def loseLife(self):
        self.lives -= 1
        self.protection = 3

    def protectionCorrection(self, dt):
        self.protection -= dt
        if self.protection < 0:
            self.protection = 0

    def end(self, hitbox, other, dir, layer):
        self.lvlUp = True
