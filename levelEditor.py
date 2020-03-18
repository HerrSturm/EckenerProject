import sys, pygame, time

#um das Level automatisch zu kopieren, installiere clipboard (pip install clipboard)
try:
    import pyperclip
except:
    print('Um das Level automatisch zu kopieren, installiere das Modul "pyperclip"\npip install pyperclip')

pygame.init()

version = '0.5.23b'

# Variabeln für Feldmarkierung
m1 = False
m2 = False
lHold = False
mHold = False
rHold = False
type = 'platform'
enemyRange = 3
printObjects = []
objects = []
cam = [0,0]

#Buttons
buttons = [
[20, 10, 40, 40, 'Material', (255,255,255)],
[200, 10, 40, 40, 'Range', (255, 60, 0)]
]

# Pygame wird initialisiert
size = width, heigth = 1400, 800
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.flip()

screen.fill((80,150,255))

#Functions----------------------------------------------------------------------

def showLevelCode():
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print('Bitte kopieren und in eine leere Level Datei einfügen:\n')
    clipboardText = '{"level": { "objects": [\n'
    if len(objects) > 0:
        print('{"level": { "objects": [')
    for i in range(0, len(printObjects)):
        if (i+1) < len(printObjects):
            suffix = ","
        else:
            suffix = ""
        print(printObjects[i] + suffix)
        clipboardText += printObjects[i] + suffix + '\n'
    if len(objects) > 0:
        print('],"characterSpawn": ['+ str(objects[0][0]/24) +', '+ str(objects[0][1]/24-4) +'],"size": [100, 100],"background": [80, 150, 255]}}')
        clipboardText += '],"characterSpawn": ['+ str(objects[0][0]/24) +', '+ str(objects[0][1]/24-4) +'],"size": [100, 100],"background": [80, 150, 255]}}'
    else:
        clipboardText = ''
    print('\n\n')
    try:
        pyperclip.copy(clipboardText)
        print('Das Level wurde automatisch in dein Clipboard kopiert!\n(Benutze in einer neuen Datei: STRG + V)\n')
    except:
        print('Um das Level automatisch zu kopieren, installiere das Modul "pyperclip"\npip install pyperclip\n')

def addObject(type, m1, m2):
    #Blockposition festlegen
    if m1[0] < m2[0]:
        posX = m1[0]-cam[0]
    else:
        posX = m2[0]-cam[0]
    if m1[1] < m2[1]:
        posY = m1[1]-cam[1]
    else:
        posY = m2[1]-cam[1]
    sizeX = abs(m2[0]-m1[0])
    sizeY = abs(m2[1]-m1[1])

    if type == 'platform':
        printObjects.append('{"type": "platform","size": [' + str(sizeX) + ',' + str(sizeY) + '],"position": [' + str(posX) + ',' + str(posY) + ']}')
        objects.append([posX*24, posY*24, sizeX*24, sizeY*24, 'platform'])
    elif type == 'grass':
        printObjects.append('{"type": "block","size": [' + str(sizeX) + ',' + str(sizeY) + '],"position":[' + str(posX) + ',' + str(posY) + '],"color": "green"}')
        objects.append([posX*24, posY*24, sizeX*24, sizeY*24, (50,100,50)])
    elif type == 'dirt':
        printObjects.append('{"type": "block","size": [' + str(sizeX) + ',' + str(sizeY) + '],"position":[' + str(posX) + ',' + str(posY) + '],"color": "brown"}')
        objects.append([posX*24, posY*24, sizeX*24, sizeY*24, (150,80,50)])
    elif type == 'stone':
        printObjects.append('{"type": "block","size": [' + str(sizeX) + ',' + str(sizeY) + '],"position":[' + str(posX) + ',' + str(posY) + '],"color": "grey"}')
        objects.append([posX*24, posY*24, sizeX*24, sizeY*24, (125,125,125)])
    elif type == 'enemy':
        printObjects.append('{"type": "enemy","size": [' + str(sizeX) + ',' + str(sizeY) + '],"position":[' + str(posX) + ',' + str(posY) + '],"range": ['+ str(enemyRange) +','+ str(enemyRange*(-1)) +']}')
        objects.append([posX*24, posY*24, sizeX*24, sizeY*24, (255,0,0)])
    elif type == 'endBlock':
        printObjects.append('{"type": "endBlock","size": [' + str(sizeX) + ',' + str(sizeY) + '],"position":[' + str(posX) + ',' + str(posY) + '],"color": "yellow"}')
        objects.append([posX*24, posY*24, sizeX*24, sizeY*24, (255,255,0)])
    showLevelCode()

def flipType(button):
    global type

    if type == 'platform':
        type = 'grass'
        button[5] = (50,100,50)
    elif type == 'grass':
        type = 'dirt'
        button[5] = (150,80,50)
    elif type == 'dirt':
        type = 'stone'
        button[5] = (125,125,125)
    elif type == 'stone':
        type = 'enemy'
        button[5] = (255,0,0)
    elif type == 'enemy':
        type = 'endBlock'
        button[5] = (255,255,0)
    elif type == 'endBlock':
        type = 'platform'
        button[5] = (255,255,255)

def flipRange():
    global enemyRange
    if enemyRange < 10:
        enemyRange += 1
    else: enemyRange = 1

def checkButton(x,y, lHold):
    global mousePos
    for button in buttons:
        if button[0] < mousePos[0] < (button[0] + button[2]):
            if button[1] < mousePos[1] < (button[1] + button[3]) and not lHold:
                if button[4] == 'Material':
                    flipType(button)
                elif button[4] == 'Range':
                    flipRange()
                return True
    return False

def update(x, y, l, r):
    global m1, m2, lHold, mHold, rHold, type

    if l == True:
        if not checkButton(x,y, lHold):
            if lHold == False and m1 == False:
                m1 = (x, y)
            elif lHold == False and m2 == False:
                m2 = (x, y)
                addObject(type, m1, m2)
        lHold = True

    else:
        lHold = False
        if m1 != False and m2 != False:
            m1 = False
            m2 = False

    if r == True:
        if rHold == False:
            rHold = True
            if len(objects) > 0:
                del objects[-1]
                del printObjects[-1]
                showLevelCode()
    else:
        rHold = False

def draw():

    if m1 != False:
        pygame.draw.rect(screen, (50,0,0), [m1[0]*24,m1[1]*24, (mouseBlockPos[0]-m1[0])*24, (mouseBlockPos[1]-m1[1])*24])
    else:
        pygame.draw.rect(screen, (50,0,0), [mouseBlockPos[0]*24,mouseBlockPos[1]*24, 24, 24])

    for array in objects:
        if array[4] == 'platform':
            pygame.draw.rect(screen, (150,80,50), [array[0]+cam[0]*24,array[1]+cam[1]*24,array[2],array[3]])
            pygame.draw.rect(screen, (50,100,50), [array[0]+cam[0]*24,array[1]+cam[1]*24,array[2],24])
        else:
            pygame.draw.rect(screen, array[4], [array[0]+cam[0]*24,array[1]+cam[1]*24,array[2],array[3]])

    pygame.draw.rect(screen, (0,0,0), [0+cam[0]*24,0+cam[1]*24,5,5])
    pygame.draw.rect(screen, (0,0,0), [1395+cam[0]*24,0+cam[1]*24,5,5])
    pygame.draw.rect(screen, (0,0,0), [0+cam[0]*24,795+cam[1]*24,5,5])
    pygame.draw.rect(screen, (0,0,0), [1395+cam[0]*24,795+cam[1]*24,5,5])
    pygame.draw.rect(screen, (0,0,0), [0+cam[0]*24,0+cam[1]*24,1400,1])
    pygame.draw.rect(screen, (0,0,0), [0+cam[0]*24,0+cam[1]*24,1,800])
    pygame.draw.rect(screen, (0,0,0), [1399+cam[0]*24,799+cam[1]*24,1,-798])
    pygame.draw.rect(screen, (0,0,0), [1399+cam[0]*24,799+cam[1]*24,-1398,1])

    for button in buttons:
        pygame.draw.rect(screen, button[5], [button[0], button[1], button[2], button[3]])

    myfont = pygame.font.SysFont('Arial', 30)
    typeText = myfont.render(type, False, (255, 255, 255))
    rangeText = myfont.render('Enemy Range: ' + str(enemyRange), False, (255, 60, 0))
    myfont = pygame.font.SysFont('Arial', 16)
    yb = myfont.render('Level-Editor by YB Version: ' + version, False, (255, 255, 200))
    screen.blit(typeText,(80,10))
    screen.blit(rangeText,(260,10))
    screen.blit(yb,(5,780))

def checkEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                cam[1] += 5
            elif event.key == pygame.K_DOWN:
                cam[1] -= 5
            elif event.key == pygame.K_LEFT:
                cam[0] += 5
            elif event.key == pygame.K_RIGHT:
                cam[0] -= 5


#-------------------------------------------------------------------------------

# Levelbauschleife
while True:
    # Screen wird bei jedem Schleifendurchlauf auf blaue Hintergrundfarbe resettet
    screen.fill((80,150,255))

#Mouse--------------------------------------------------------------------------
    #Mouse position in pixels
    mousePos = pygame.mouse.get_pos()
    #Mouse position in blocks
    mouseBlockPos = (int(mousePos[0]/24), int(mousePos[1]/24))
    #Wird eine Maustaste gedrückt?
    click = pygame.mouse.get_pressed()
    #print('Maus Position: ' + str(mouseBlockPos) + ' | Maus geklickt: ' + str(click))
#-------------------------------------------------------------------------------

    update(mouseBlockPos[0], mouseBlockPos[1], click[0], click[2])
    draw()

    # Handles the shutting down of the programm, ignorieren!
    checkEvents()

    dt = clock.get_time() / 1000.0 # Zeit seit dem letzten tick (Frame) in Sek.
    clock.tick(60) # Kontrolliert die Aktuallisierungen pro Minute (FPS)

    pygame.display.flip()
