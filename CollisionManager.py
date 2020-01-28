from Layer import LayerMap

DT = 1 / 60

class CollisionManager(object):

    class _CollisionManager:

        def __init__(self):
            self.hitBoxes = set()
            self.layerMap = LayerMap()
            self.acc = 0

        def add(self, hitBox):
            self.hitBoxes.add(hitBox)

        def remove(self, hitBox):
            self.hitBoxes.remove(hitBox)

        def update(self, dt):
            self.acc += dt
            while self.acc >= DT:
                self._physics(DT)
                self.acc -= DT

        def _physics(self, dt):
            for hitBox in self.hitBoxes:
                if hitBox.static:
                    continue
                near = self.getNearHitBoxes(hitBox)
                hitBox.pos.x += hitBox.vel.x * dt
                for other in near:
                    if not self.layerMap.matches(hitBox.layer, other.layer):
                        continue
                    if hitBox.overlap(other):
                        if hitBox.right > other.left and hitBox.vel.x > 0:
                            hitBox.right = other.left
                            hitBox.vel.x = 0
                            hitBox._collide(other)
                        if hitBox.left < other.right and hitBox.vel.x < 0:
                            hitBox.left = other.right
                            hitBox.vel.x = 0
                            hitBox._collide(other)
                hitBox.pos.y += hitBox.vel.y * dt
                for other in near:
                    if not self.layerMap.matches(hitBox.layer, other.layer):
                        continue
                    if hitBox.overlap(other):
                        if hitBox.bottom > other.top and hitBox.vel.y > 0:
                            hitBox.bottom = other.top
                            hitBox.vel.y = 0
                            hitBox._collide(other)
                        if hitBox.top < other.bottom and hitBox.vel.y < 0:
                            hitBox.top = other.bottom
                            hitBox.vel.y = 0
                            hitBox._collide(other)

        def getNearHitBoxes(self, hitBox):
            return list(filter(lambda h: h != hitBox, self.hitBoxes))

    instance = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = CollisionManager._CollisionManager()
        return cls.instance
