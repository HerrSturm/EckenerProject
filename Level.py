import json
from Character import *
from Block import *
from GegnerClass import *
from Camera import *

colors = {
    "brown": (150,80,50),
    "blue": (80,150,255),
    "green": (50,100,50),
    "grey": (125,125,125),
    "goal": (212,175,55)
}

class Level:

    def __init__(self, objects, characterSpawn, size, background, filename):
        self.objects = objects
        self.filename = filename
        self.character = Character(characterSpawn) # TODO: use characterSpawn
        self.objects.append(self.character)
        self.camera = Camera(size * 24, background)
        self.camera.moveToCenter(self.character.hitBox.center)

    def loadFile(name):
        file = open(name)
        return Level.load(json.load(file),name)

    def load(json, filename):
        objects = []
        level = json["level"]
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
                    object["range"][0],
                    object["range"][1]
                ))
        characterSpawn = Vec2(*level["characterSpawn"])
        size = Vec2(*level["size"])
        background = tuple(level["background"])
        return Level(objects, characterSpawn, size, background, filename)

    def update(self, dt):
        for object in self.objects:
            object.update(dt)
        if self.death():
            self.restore()
        self.camera.glideCenter(self.character.hitBox.center, dt)
        CollisionManager().update(dt)

    def draw(self):
        for object in self.objects:
            object.draw(self.camera.surface)
        self.camera.draw()

    def remove(self):
        for object in self.objects:
            object.remove()

    def restore(self):
        file = open(self.filename)
        map = json.load(file)
        objects = []
        level = map["level"]
        characterSpawn = Vec2(*level["characterSpawn"])
        self.character.hitBox.pos.values = characterSpawn * 24


    def death(self):
        if self.character.hitBox.pos.y > 50*24:
            self.character.lives -= 1
            if self.character.lives<=0:
                return True
            else:
                return False
