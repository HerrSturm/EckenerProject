import Vec2

class HitBox:
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.vel = Vec2()

    def getLeft(self):
        return self.pos.x

    def setLeft(self, left):
        self.pos.x = left

    left = property(getLeft, setLeft)

    def getRight(self):
        return self.pos.x + self.size.x

    def setRight(self, right):
        self.pos.x = right - self.size.x

    right = property(getRight, setRight)

    def getTop(self):
        return self.pos.y

    def setTop(self, top):
        self.pos.y = top

    top = property(getTop, setTop)

    def getBottom(self):
        return self.pos.y + self.size.y

    def setBottom(self,  bottom):
        self.pos.y = bottom - self.size.y

    bottom = property(getBottom, setBottom)

    def overlap(self, other):
        return (
            self.left < other.right and
            self.right > other.left and
            self.top > other.bottom and
            self.bottom < other.top)
