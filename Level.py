import json
from Character import *
from Block import *
from GegnerClass import *
from Camera import *
from Vec2 import *
from FollowingEnemy import *
from cannon import *

colors = {
    "brown": (150,80,50),
    "blue": (80,150,255),
    "green": (50,100,50),
    "grey": (125,125,125),
    "goal": (212,175,55)
}

class Level:

    def __init__(self, objects, characterSpawn, size, background):
        self.objects = objects
        self.characterSpawn = characterSpawn * 24
        self.character = Character(self.characterSpawn)
        self.objects.append(self.character)
        self.size = size * 24
        self.camera = Camera(self.size, background)
        self.camera.moveToCenter(self.character.hitBox.center)
        self.gameOver = False

    def loadFile(name):
        file = open(name)
        return Level.load(json.load(file))

    def load(json):
        objects = []
        level = json["level"]
        for object in level["objects"]:

            #color to texture
            if object["type"] == "block" or object["type"] == "movingBlock":
                if object["color"] == 'green':
                    object["texture"] = 'grass'
                elif object["color"] == 'brown':
                    object["texture"] = 'dirt'
                elif object["color"] == 'grey':
                    object["texture"] = 'stone'

            if object["type"] == "block":
                objects.append(Block(
                    Vec2(*object["position"]),
                    Vec2(*object["size"]),
                    colors[object["color"]],
                    object["texture"]
                ))

            #create a simple platform with a grass surface
            if object["type"] == "platform":
                objects.append(Block(
                    Vec2(*object["position"]),
                    Vec2(*[object["size"][0],1]),
                    colors["green"],
                    'grass'
                ))
                objects.append(Block(
                    Vec2(*[object["position"][0], object["position"][1]+1]),
                    Vec2(*[object["size"][0],object["size"][1]-1]),
                    colors["brown"],
                    'dirt'
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

            if object["type"] == "cannon":
                objects.append(Cannon(
                    Vec2(*object["position"]),
                    Vec2(*object["size"])
                ))

            if object["type"] == "cannonBall":
                objects.append(CannonBall(
                    Vec2(*object["position"]),
                    Vec2(*object["size"]),
                    object["range"][0],
                    object["range"][1]
                ))
                
            if object["type"] == "FollowingEnemy":
                objects.append(FollowingEnemy(
                    Vec2(*object["position"]),
                    Vec2(*object["size"]),
                    object["range"][0],
                    object["range"][1]
                ))

            if object["type"] == "movingBlock":
                objects.append(MovingBlock(
                    Vec2(*object["position"]),
                    Vec2(*object["size"]),
                    object["range"][0],
                    object["range"][1],
                    colors[object["color"]],
                    object["texture"]
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
        self.checkCharacterFallDeath()

    def checkCharacterFallDeath(self):
        if self.character.hitBox.top > self.size.y:
            self.character.loseLife()
            self.character.hitBox.setPos(self.characterSpawn)
            self.character.hitBox.vel = Vec2()

    def draw(self):
        for object in self.objects:
            object.draw(self.camera.surface)
        self.camera.draw()

        for live in range(0, self.character.lives):
            self.camera.mainScreen.blit(self.character.heartImage, (20 + live*50, 20))

    def remove(self):
        for object in self.objects:
            object.remove()
