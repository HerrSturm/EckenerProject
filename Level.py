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
    "yellow": (255,255,0)
}

class Level:

    def __init__(self, objects, characterSpawn, size, background):
        self.objects = objects
        self.character = Character(characterSpawn) # TODO: use characterSpawn
        self.objects.append(self.character)
        self.camera = Camera(size * 24, background)
        self.camera.moveToCenter(self.character.hitBox.center)
        self.gameOver = False

    def loadFile(name):
        file = open(name)
        return Level.load(json.load(file))

    def load(json):
        objects = []
        level = json["level"]
        for object in level["objects"]:
            if object["type"] == "block":
                objects.append(Block(
                    Vec2(*object["position"]),
                    Vec2(*object["size"]),
                    colors[object["color"]]
                ))

            #create a simple platform with a grass surface
            if object["type"] == "platform":
                objects.append(Block(
                    Vec2(*object["position"]),
                    Vec2(*[object["size"][0],1]),
                    colors["green"]
                ))
                objects.append(Block(
                    Vec2(*[object["position"][0], object["position"][1]+1]),
                    Vec2(*[object["size"][0],object["size"][1]-1]),
                    colors["brown"]
                ))

            #creating an EndBlock object
            if object["type"] == "endBlock":
                objects.append(EndBlock(
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
        return Level(objects, characterSpawn, size, background)

    def update(self, game, dt):
        for object in self.objects:
            object.update(game, dt)
        self.camera.glideCenter(self.character.hitBox.center, dt)
        CollisionManager().update(dt)

    def draw(self):
        for object in self.objects:
            object.draw(self.camera.surface)
        self.camera.draw()

        for live in range(0, self.character.lives):
            self.camera.mainScreen.blit(self.character.heartImage, (20 + live*50, 20))

    def remove(self):
        for object in self.objects:
            object.remove()
