from Vec2 import Vec2
from Layer import Layer

## TODO: destructor

class HitBox(object):
    def __init__(self, pos, size, static, layer, vel = Vec2()):
        self.pos = pos
        self.size = size
        self.vel = vel
        self.static = static
        self.layer = layer
        self.callbacks = []

    @property
    def left(self):
        return self.pos.x

    @left.setter
    def left(self, left):
        self.setX(left)

    @property
    def right(self):
        return self.pos.x + self.size.x

    @right.setter
    def right(self, right):
        self.setX(right - self.size.x)

    @property
    def top(self):
        return self.pos.y

    @top.setter
    def top(self, top):
        self.setY(top)

    @property
    def bottom(self):
        return self.pos.y + self.size.y

    @bottom.setter
    def bottom(self,  bottom):
        self.setY(bottom - self.size.y)

    def setX(self, x):
        self.setPos(Vec2(x, self.pos.y))

    def setY(self, y):
        self.setPos(Vec2(self.pos.x, y))

    def setPos(self, pos):
        self.pos = pos
        [callback(self) for (type, callback) in self.callbacks if type == "pos"]

    def onPosChanged(self, callback):
        self.callbacks.append(("pos", callback))

    def onCollide(self, callback):
        self.callbacks.append(("collide", callback))

    def _collide(self, other):
        [callback(self, other) for (type, callback) in self.callbacks
            if type == "collide"]

    def overlap(self, other):
        return (
            self.left < other.right and
            self.right > other.left and
            self.top < other.bottom and
            self.bottom > other.top)
