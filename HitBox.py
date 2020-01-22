import Vec2
from Vec2 import Vec2

class HitBox:
class HitBox(object):
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.vel = Vec2()

    def getLeft(self):
        return self.pos.x

    def setLeft(self, left):
        self.setX(left)

    left = property(getLeft, setLeft)

    def getRight(self):
        return self.pos.x + self.size.x

    def setRight(self, right):
        self.setX(right - self.size.x)

    right = property(getRight, setRight)

    def getTop(self):
        return self.pos.y

    def setTop(self, top):
        self.setY(top)

    top = property(getTop, setTop)

    def getBottom(self):
        return self.pos.y + self.size.y

    def setBottom(self,  bottom):
        self.setY(bottom - self.size.y)

    def setX(self, x):
        self.setPos(Vec2(x, self.pos.y))

    def setY(self, y):
        self.setPos(Vec2(self.pos.x, y))

    bottom = property(getBottom, setBottom)

    def setPos(self, pos):
        self.pos = pos

    def overlap(self, other):
        return (
            self.left < other.right and
            self.right > other.left and
            self.top > other.bottom and
            self.bottom < other.top)
