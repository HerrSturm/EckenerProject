import pygame
from HitBox import*
from random import randint
from Direction import Direction
from GameState import GameState
from sprites import runSprites, fallSprites, idleSprites, wallSlideSprites, saltoSprites, crouchSprites, attackSprites
pygame.mixer.init(48000, -16, 2, 512)
sliding = pygame.mixer.Sound("Sounds/slidingwav.wav")
bgmusic = pygame.mixer.Sound("Sounds/backgroundmusic.wav")
screams = [pygame.mixer.Sound("Sounds/ahh.wav"),pygame.mixer.Sound("Sounds/aaa.wav"),pygame.mixer.Sound("Sounds/scream8.wav")]
runSound = pygame.mixer.Sound("Sounds/runSound.wav")

bgmusic.set_volume(0.1)
sliding.set_volume(0.1)
bgmusic.play(-1)
#CONST gravity
class Character():
    GRAVITY = 300
    JUMPVEL = 275
    MOVEVEL = 200
    def __init__(self, position): #Vec2 position
        self.heading = 1
        self.mainScreen = pygame.display.get_surface()
        self.spriteCount = 2
        self.imageoriginal = runSprites(self.spriteCount)
        self.imagebig = pygame.transform.scale(self.imageoriginal, (125, 75))
        self.isGrounded = False
        self.isGrounded_ = False
        self.isCrouching = False
        self.health = 1
        self.isSliding = False
        self.wasSliding = False
        self.isRunning = False
        self.wasRunning = False
        size = Vec2(40,58)
        self.lives = 3
        self.protection = 3 #in sekunden nach Lebensverlust angegeben
        self.heartImage = pygame.image.load('Graphics/GUI/heart.png')
        self.lvlUp = False
        self.nextLvl = 2
        self.hitBox = HitBox(position, size, False, Layer("player"),Vec2(0,0))
        self.hitBox.onCollide(self.check_Grounded)
        self.hitBox.onCollide(self.hurt, Layer("deadly"))
        self.hitBox.onCollide(self.end, Layer("end"))
        CollisionManager().onBeforeUpdate(self.beforeCollisionManager)
        CollisionManager().onAfterUpdate(self.afterCollisionManager)
        self.mainScreen = pygame.display.get_surface()
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
        keys = pygame.key.get_pressed()
        self.isSliding = False
        #checks if the "s" button is pressed and the character is therefore "crouching"
    #CROUCH
        if keys[pygame.K_s] and self.isGrounded:
            self.isCrouching = True
        else:
            self.isCrouching = False
        #pygame.draw.rect(surface, (0, 0, 0), (self.hitBox.pos.values[0], self.hitBox.pos.values[1], self.hitBox.size.values[0], self.hitBox.size.values[1]))
        self.isRunning = False
        if self.isGrounded == True and self.hitBox.vel.x == 0 and self.isCrouching:
            self.imageoriginal = crouchSprites(self.spriteCount)
            self.imagebig = pygame.transform.scale(self.imageoriginal, (125, 75))
    #IDLE
        elif self.isGrounded == True and self.hitBox.vel.x == 0:
            self.imageoriginal = idleSprites(self.spriteCount)
            self.imagebig = pygame.transform.scale(self.imageoriginal, (125, 75))
    #SLIDE
        elif self.isGrounded == False and self.hitBox.vel.x == 0 and self.hitBox.vel.y >= 0 and keys[pygame.K_a]:
            self.imageoriginal = wallSlideSprites(self.spriteCount)
            self.imagebig = pygame.transform.scale(self.imageoriginal, (125, 75))
            self.isSliding = True
        elif self.isGrounded == False and self.hitBox.vel.x == 0 and self.hitBox.vel.y >= 0 and keys[pygame.K_d]:
            self.imageoriginal = wallSlideSprites(self.spriteCount)
            self.imagebig = pygame.transform.scale(self.imageoriginal, (125, 75))
            self.isSliding = True
    #CROUCH
        elif self.isGrounded == True and self.isCrouching:
            self.imageoriginal = crouchSprites(self.spriteCount)
            self.imagebig = pygame.transform.scale(self.imageoriginal, (125, 75))
    #IDLE & RUN
        elif self.isGrounded == True:
            if self.hitBox.vel.x == self.movingSolid and not self.updateKeys():
                self.imageoriginal = idleSprites(self.spriteCount)
                self.imagebig = pygame.transform.scale(self.imageoriginal, (125, 75))
            else:
                self.imageoriginal = runSprites(self.spriteCount)
                self.imagebig = pygame.transform.scale(self.imageoriginal, (125, 75))
                self.isRunning = True
    #CROUCH
        elif self.isGrounded == True and self.isCrouching:
            self.imageoriginal = crouchSprites(self.spriteCount)
            self.imagebig = pygame.transform.scale(self.imageoriginal, (125, 75))
    #JUMP
        elif self.isGrounded == False and self.hitBox.vel.y <= -20:
            self.imageoriginal = pygame.image.load("Graphics/aAllGraphics/Adventurer/adventurer-jump-02.png").convert_alpha()
            self.imagebig = pygame.transform.scale(self.imageoriginal, (125, 75))
        elif self.isGrounded == False and self.hitBox.vel.y > -20 and self.hitBox.vel.y <= 20:
            self.imageoriginal = pygame.image.load("Graphics/aAllGraphics/Adventurer/adventurer-jump-03.png").convert_alpha()
            self.imagebig = pygame.transform.scale(self.imageoriginal, (125, 75))
        elif self.isGrounded == False:
            self.imageoriginal = fallSprites(self.spriteCount)
            self.imagebig = pygame.transform.scale(self.imageoriginal, (125, 75))
    #HEADING
        if self.hitBox.vel.x > 0 and not self.hitBox.vel.x == self.movingSolid:
            self.heading = 1
        elif self.hitBox.vel.x < 0 and not self.hitBox.vel.x == self.movingSolid:
            self.heading = -1
        #self.imagebig = pygame.transform.scale(saltoSprites(self.spriteCount), (125, 75))
        if self.heading == -1:
            self.imagebig = pygame.transform.flip(self.imagebig,True,False)
    #SLIDE
        if self.isSliding and keys[pygame.K_a]:
            surface.blit(self.imagebig, ((self.hitBox.pos.x)-45,(self.hitBox.pos.y)-15))
        elif self.isSliding and keys[pygame.K_d]:
            surface.blit(self.imagebig, ((self.hitBox.pos.x)-40,(self.hitBox.pos.y)-15))
        else:
            surface.blit(self.imagebig, ((self.hitBox.pos.x)-50,(self.hitBox.pos.y)-15))
        self.spriteCount = self.spriteCount + 1
        if self.isSliding == True:
            self.GRAVITY = 1
        if self.isSliding and keys[pygame.K_s]:
            self.GRAVITY = 360
        elif self.isSliding == True:
            self.GRAVITY = 90
        elif keys[pygame.K_s]:
            self.GRAVITY = 1200
        else:
            self.GRAVITY = 300
        if self.isSliding and self.wasSliding == False:
            pygame.mixer.music.set_volume(0.25)
            sliding.play(-1)
        elif self.isSliding == False and self.wasSliding:
            sliding.stop()
        if self.isSliding == True:
            self.wasSliding = True
        else:
            self.wasSliding = False
    #RUN
        if self.isRunning and self.wasRunning == False:
            runSound.play(-1)
        if self.isRunning == False and self.wasRunning:
            runSound.stop()
        if self.isRunning == True:
            self.wasRunning = True
        else:
            self.wasRunning = False
    #updates the player
    def update(self, game, dt):
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
    #def playsound(self):

    def updateKeys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.moveleft()
        if keys[pygame.K_d]:
            self.moveright()
        if keys[pygame.K_w]:
            self.jump()

        if keys[pygame.K_a]==False and keys[pygame.K_d]==False:
            self.standstill()
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
        if self.isGrounded:
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
        screams[randint(0,len(screams)-1)].play()
    def protectionCorrection(self, dt):
        self.protection -= dt
        if self.protection < 0:
            self.protection = 0

    def end(self, hitbox, other, dir, layer):
        self.lvlUp = True
