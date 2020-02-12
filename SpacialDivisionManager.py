class SpacialDivisionManager:
    pass


class Cell:

    def __init__(self, size):
        self.size = size
        self.cells = dict()

    def add(self, hitBox):
        posIndex = hitBox.pos // self.size
        posIndex = frozenset(index.values)
        sizeIndex = hitBox.pos // self.size
        sizeIndex = frozenset(index.values)
        if self.cells[index]:
            pass
