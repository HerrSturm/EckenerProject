from HitBox import *
#playerHitBox = HitBox(vec2(100,100),vec2(100,100),False,Layer("player"),vec2(0,0))

def moveright(self):
    playerHitBoxVel = self.vel()
    if playerHitBoxVel <= 10:
        playerHitBox.vel = vec2(playerHitBoxVel+1,0)       #hitbox bewegt sich nach rechts


def moveleft(self):
    playerHitBoxVel = self.vel()
    if playerHitBoxVel >= -10:
        playerHitBox.vel = vec2 (playerHitBoxVel-1,0)      #hitbox bewegt sich nach links
