class Object:

    def __init__(self, pos, size, static, layer, drawable):
        self.hitBox = HitBox(pos, size, static, layer)
        self.drawable = drawable

    def update(self, dt):
        self.drawable.update(dt)

    def draw(self):
        self.drawable.draw(pos)
