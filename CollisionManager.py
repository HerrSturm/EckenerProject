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
            pass

    instance = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = CollisionManager._CollisionManager()
        return cls.instance
