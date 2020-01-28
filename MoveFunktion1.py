from HitBox import *
#playerHitBox = HitBox(vec2(100,100),vec2(100,100),False,Layer("player"),vec2(0,0))

def moveright(self):                            #Funktion um die Hitbox nach rechts zu bewegen (geschw. auf +1)
    playerHitBoxVel = self.vel()
    if playerHitBoxVel <= 10:
        playerHitBox.vel = vec2(1,0)            #hitbox bewegt sich nach rechts


def moveleft(self):                             #Funktion um die Hitbox nach links zu bewegen (geschw. auf -1)
    playerHitBoxVel = self.vel()
    if playerHitBoxVel >= -10:
        playerHitBox.vel = vec2 (-1,0)          #hitbox bewegt sich nach links


def standstill(self):                           #Funktion um die Hitbox zum stehen zu bringen (geschw. auf 0)
    playerHitBoxVel = self.vel()
    playerHitBox.Vel = vec2 (0,0)               #Hitbox bleibt stehen
