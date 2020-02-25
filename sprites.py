#Hier befinden sich alle Sprites, die in der Animation verwendet werden sollen.
def runSprites(x):
    SpritesRun = ["Graphics/aAllGraphics/Adventurer/adventurer-run-00.png","Graphics/aAllGraphics/Adventurer/adventurer-run-01.png",
        "Graphics/aAllGraphics/Adventurer/adventurer-run-02.png","Graphics/aAllGraphics/Adventurer/adventurer-run-03.png",
        "Graphics/aAllGraphics/Adventurer/adventurer-run-04.png","Graphics/aAllGraphics/Adventurer/adventurer-run-05.png"]
    return(SpritesRun[x//10%len(SpritesRun)-1])
