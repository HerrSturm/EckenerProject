colors = {
    "brown": (150,80,50),
    "blue": (80,150,255),
    "green": (50,100,50)
}

class Level:

    def __init__(self, objects, characterSpawn):
        self.objects = objects
        self.character = Character() # TODO: use characterSpawn
        self.objects.append(self.character)

    def load(json):
        objects = []
        for object in level["objects"]:
            if object["type"] == "block":
                objects.append(Block(
                    Vec2(*object["position"]),
                    Vec2(*object["size"]),
                    colors[object["color"]]
                ))
            if object["type"] == "enemy":
                objects.append(Gegner(
                    Vec2(*object["position"]),
                    Vec2(*object["size"]),
                    object["range"][0]
                    object["range"][1]
                ))
        characterSpawn = Vec2(*level["characterSpawn"])
        return Level(objects, characterSpawn)

    def update(self, dt):
        for object in self.objects:
            object.update()
        CollisionManager().update(dt)
