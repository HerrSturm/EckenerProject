#Hier befinden sich alle Sprites, die in der Animation verwendet werden sollen.
def runSprites(x):
    path = "Graphics/aAllGraphics/Adventurer/"
    SpritesRun = ["adventurer-run-00.png","adventurer-run-01.png",
        "adventurer-run-02.png","adventurer-run-03.png",
        "adventurer-run-04.png","adventurer-run-05.png"]
    return(str(path)+str(SpritesRun[x//10%len(SpritesRun)-1]))
def fallSprites(x):
    path = "Graphics/aAllGraphics/Adventurer/"
    SpritesFall = ["adventurer-fall-00.png","adventurer-fall-01.png"]
    return(path+SpritesFall[x//10%len(SpritesFall)-1])
def idleSprites(x):
    path = "Graphics/aAllGraphics/Adventurer/"
    SpritesIdle = ["adventurer-idle-00.png","adventurer-idle-01.png","adventurer-idle-02.png"]
    return(path+SpritesIdle[x//15%len(SpritesIdle)-1])   
