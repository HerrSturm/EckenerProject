import pygame
from HitBox import*
#CONST gravity
class Character():
    def __init__(self, position): #Vec2 position
        self.isGrounded = False
        self.GRAVITY = 10
        self.JUMPVEL = 100
        self.vel = Vec2(0,0)
        size = Vec2(150,150)
        self.hitBox = HitBox(position, size, False, Layer("player"),vel)
        self.hitBox.onCollide(check_Grounded)
        CollisionManager().beforeUpdate(beforeCollisionManager)
        CollisionManager().afterUpdate(afterCollisionManager)
        self.mainScreen = pygame.display.get_surface()
        pygame.draw.rect(self.mainScreen, (255, 255, 255), (self.hitBox.pos.values[0], self.hitBox.pos.values[1], self.hitBox.size.values[0], self.hitBox.size.values[1]))

    def check_Grounded(self, other, dir):
        if dir == Direction.DOWN:
            self.isGrounded = True

    def update(self, dt):
        pygame.draw.rect(self.mainScreen, self.shape)

    def beforeCollisionManager():
        self.isGrounded = False
        self.vel += Vec2(0, -self.GRAVITY*dt)

    def afterCollisionManager():
        #after col update
        self.testGrounded = False
        if isGrounded:
            self.vel.y = 0
            if jump: #jump command given
                self.vel += Vec2(0, self.JUMPVEL)
