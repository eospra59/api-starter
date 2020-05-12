import pygame
import random

win = pygame.display.set_mode((800, 600))
img = pygame.image.load('assets/gfx/Overworld.png').convert()
caveimg = pygame.image.load('assets/gfx/cave.png').convert()
treeimg = pygame.image.load('assets/gfx/objects.png').convert()

pygame.font.init()

grass = pygame.Surface([32, 30]).convert()
grass.blit(img, (0, 0), (0, 145, 32, 30))
water = pygame.Surface([32, 30]).convert()
water.blit(img, (0, 0), (0, 17, 32, 30))
pit = pygame.Surface([32, 30]).convert()
pit.blit(img, (0, 0), (240, 370, 32, 30))
rock = pygame.Surface([32, 30]).convert() #water rock
rock.blit(caveimg, (0, 0), (145, 115, 32, 30))
tree = pygame.Surface([32, 30]).convert()
tree.blit(treeimg, (0, 0), (190, 190, 32, 30))
dirt = pygame.Surface([32, 30]).convert()
dirt.blit(img, (0, 0), (200, 210, 32, 30))
rock2 = pygame.Surface([32, 30]).convert() #grass rock
rock2.blit(img, (0, 0), (145, 178, 32, 30))
hut = pygame.Surface([32, 30]).convert()
hut.blit(img, (0, 0), (208, 90, 32, 30))
wood = pygame.Surface([32, 30]).convert()
wood.blit(img, (0, 0), (65, 200, 32, 30))
stone = pygame.Surface([32, 30]).convert()
stone.blit(img, (0, 0), (128, 355, 32, 30))
stump = pygame.Surface([32, 30]).convert()
stump.blit(treeimg, (0, 0), (0, 195, 32, 30))
trap = pygame.Surface([32, 30]).convert()
trap.blit(caveimg, (0, 0), (130, 10, 32, 30))
box = pygame.Surface([32, 30]).convert()
box.blit(img, (0, 0), (560, 130, 32, 30))



row = []
for j in range(25):
    tempRow = []
    for i in range(25):
        num = random.randint(0, 3)
        tempRow.append(num)
    row.append(tempRow)

ter = 0  
timer = 0
dt = 0
a = 0
b = 0
c = 0
d = 0
m = 0 
w = 0

BLUE = (0, 0, 100)
CYAN = (100, 100, 100)
black = (0, 0, 0)
def build():
   for i in range(25):
            for j in range(25):
                if row[i][j] == 0:
                    win.blit(a, (i * 32, j * 30))
                if row[i][j] == 1:
                    win.blit(b, (i * 32, j * 30))
                if row[i][j] == 2:
                    win.blit(c, (i * 32, j * 30))
                if row[i][j] == 3:
                    win.blit(d, (i * 32, j * 30)) 

def edit():
    global timer
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            if timer == 0:  # First mouse click.
                timer = 0.001  # Start the timer.
                # Set the x, y postions of the mouse click
                x, y = event.pos
                i = x // 32
                j = y // 30
                row[i][j] = m
                # Click again before 0.5 seconds to double click.
            elif timer < 0.5:
                x, y = event.pos
                i = x // 32
                j = y // 30
                row[i][j] = w
                timer = 0
        # Increase timer after mouse was pressed the first time.
        if timer != 0:
            timer += dt
            # Reset after 0.5 seconds.
            if timer >= 0.5:
                print('too late')
                timer = 0

def text_objects(text, font):
    textSurface = font.render(text, True, BLUE)
    return textSurface, textSurface.get_rect()

def button (msg, x, y, w, h, ic, ac, action=None ):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if (x+w > mouse[0] > x) and (y+h > mouse[1] > y):
        pygame.draw.rect(win, CYAN, (x, y, w, h))
        if (click[0] == 1 and action != None):
            if  (action == "Ocean"):
                ter = "ocean"
            elif  (action == "Forest"):
                ter = "forest"
            elif  (action == "Desert"):
                ter = "desert"
            elif  (action == "Town"):
                ter = "town"
            elif  (action == "Fields"):
                ter = "fields"
            elif  (action == "Dungeon"):
                ter = "dungeon"

    else:
        pygame.draw.rect(win, BLUE, (x, y, w, h))
        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        win.blit(textSurf, textRect)

button("Ocean", 0, 50, 100, 50, BLUE, CYAN, action="Ocean")
button("Forest", 100, 50, 100, 50, BLUE, CYAN, action="Forest")
button("Desert", 200, 50, 100, 50, BLUE, CYAN, action="Desert")
button("Town", 300, 50, 100, 50, BLUE, CYAN, action="Town")
button("Fields", 500, 50, 100, 50, BLUE, CYAN, action="Fields")
button("Dungeon", 500, 50, 100, 50, BLUE, CYAN, action="Dungeon")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))

    if ter == "ocean":
        a = water
        b = water
        c = rock
        d = water
        build()
        m = 1
        w = 2
        edit()


    if ter == "forest":
        a = grass
        b = tree
        c = tree
        d = tree
        build()
        m = 0
        w = 2
        edit()
        
    if ter == "desert":
        a = rock2
        b = dirt
        c = dirt
        d = dirt
        build()
        m = 1
        w = 0
        edit()

    if ter == "town":
        a = hut
        b = stone
        c = tree
        d = stone
        build()
        m = 1
        w = 0
        edit()

    if ter == "fields":
        a = grass
        b = grass
        c = stump
        d = grass
        build()
        m = 1
        w = 0
        edit()
        
    if ter == "dungeon":
        a = pit
        b = wood
        c = box
        d = wood
        build()
        m = 1
        w = 2
        edit()

    pygame.display.update()

pygame.quit()
