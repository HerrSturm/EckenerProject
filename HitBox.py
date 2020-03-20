from Vec2 import Vec2
from Layer import Layer
from CollisionManager import CollisionManager

class HitBox(object):
    def __init__(self, pos, size, static, layer, vel = Vec2()):
        self.pos = Vec2(pos)
        self.size = Vec2(size)
        self.vel = Vec2(vel)
        self.static = static
        self.layer = layer
        self.callbacks = []
        CollisionManager().add(self)

    def remove(self):
        CollisionManager().remove(self)

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
        self.pos = Vec2(pos)
        for tup in self.callbacks:
            if tup[0] == "pos":
                #pylint: disable = unused-variable
                (name, callback) = tup
                callback(self)

    @property
    def center(self):
        return self.pos + self.size / 2

    def onPosChanged(self, callback):
        self.callbacks.append(("pos", callback))

    def onCollide(self, callback, layer = Layer.all()):
        self.callbacks.append(("collide", callback, layer))

    def _collide(self, other, dir):
        for tup in self.callbacks:
            if tup[0] == "collide":
                #pylint: disable = unused-variable
                (name, callback, layer) = tup
                if other.layer == layer:
                    callback(self, other, dir, layer)

    def listensToCollisionLayer(self, listenLayer):
        for tup in self.callbacks:
            if tup[0] == "collide":
                #pylint: disable = unused-variable
                (name, callback, layer) = tup
                if layer == listenLayer:
                    return True
        return False

    def hasLayer(self, layer):
        return layer == self.layer

    def overlap(self, other):
        return (
            self.left < other.right and
            self.right > other.left and
            self.top < other.bottom and
            self.bottom > other.top)
