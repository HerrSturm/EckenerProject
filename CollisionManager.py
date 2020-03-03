from Layer import LayerMap
from Direction import Direction

DT = 1 / 60

class CollisionManager(object):

    class _CollisionManager:

        def __init__(self):
            self.hitBoxes = set()
            self.layerMap = LayerMap()
            self.acc = 0
            self.callbacks = []

        def add(self, hitBox):
            self.hitBoxes.add(hitBox)

        def remove(self, hitBox):
            if hitBox in self.hitBoxes:
                self.hitBoxes.remove(hitBox)

        def update(self, dt):
            self.acc += dt
            while self.acc >= DT:
                self._physics(DT)
                self.acc -= DT

        def _physics(self, dt):
            self._callCallbacks("beforeUpdate", dt)
            for hitBox in self.hitBoxes:
                near = self.getNearHitBoxes(hitBox)
                hitBox.pos.x += hitBox.vel.x * dt
                for other in near:
                    trigger = hitBox.listensToCollisionLayer(other.layer)
                    move = self.layerMap.matches(hitBox.layer, other.layer)
                    if not (move or trigger):
                        continue
                    if hitBox.static:
                        continue
                    if hitBox.overlap(other):
                        if hitBox.right > other.left and hitBox.vel.x > 0:
                            if move:
                                hitBox.right = other.left
                                hitBox.vel.x = 0
                            hitBox._collide(other, Direction.RIGHT)
                        if hitBox.left < other.right and hitBox.vel.x < 0:
                            if move:
                                hitBox.left = other.right
                                hitBox.vel.x = 0
                            hitBox._collide(other, Direction.LEFT)
                hitBox.pos.y += hitBox.vel.y * dt
                for other in near:
                    trigger = hitBox.listensToCollisionLayer(other.layer)
                    move = self.layerMap.matches(hitBox.layer, other.layer)
                    if not (move or trigger):
                        continue
                    if hitBox.static:
                        continue
                    if hitBox.overlap(other):
                        if hitBox.bottom > other.top and hitBox.vel.y > 0:
                            if move:
                                hitBox.bottom = other.top
                                hitBox.vel.y = 0
                            hitBox._collide(other, Direction.DOWN)
                        if hitBox.top < other.bottom and hitBox.vel.y < 0:
                            if move:
                                hitBox.top = other.bottom
                                hitBox.vel.y = 0
                            hitBox._collide(other, Direction.UP)
            self._callCallbacks("afterUpdate", dt)

        def _callCallbacks(self, event, dt):
            [callback(dt) for (type, callback) in self.callbacks
                if type == event]

        def onBeforeUpdate(self, callback):
            self.callbacks.append(("beforeUpdate", callback))

        def onAfterUpdate(self, callback):
            self.callbacks.append(("afterUpdate", callback))

        def getNearHitBoxes(self, hitBox):
            return list(filter(lambda h: h != hitBox, self.hitBoxes))

    instance = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = CollisionManager._CollisionManager()
        return cls.instance
