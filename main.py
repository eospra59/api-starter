import pygame
import random

win = pygame.display.set_mode((800, 600))
img = pygame.image.load('assets/gfx/Overworld.png').convert()
caveimg = pygame.image.load('assets/gfx/cave.png').convert()
treeimg = pygame.image.load('assets/gfx/objects.png').convert()


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


row = []
for j in range(25):
    tempRow = []
    for i in range(25):
        num = random.randint(0, 3)
        tempRow.append(num)
    row.append(tempRow)
    
ter = input("What type of terrain would you like?")
timer = 0
dt = 0


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))

    if ter == "ocean":
        for i in range(25):
            for j in range(25):
                if row[i][j] == 0:
                    win.blit(water, (i * 32, j * 30))
                if row[i][j] == 1:
                    win.blit(water, (i * 32, j * 30))
                if row[i][j] == 2:
                    win.blit(rock, (i * 32, j * 30))
                if row[i][j] == 3:
                    win.blit(water, (i * 32, j * 30))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if timer == 0:  # First mouse click.
                    timer = 0.001  # Start the timer.
                    # Set the x, y postions of the mouse click
                    x, y = event.pos
                    i = x // 32
                    j = y // 30
                    row[i][j] = 1
                    # Click again before 0.5 seconds to double click.
                elif timer < 0.5:
                    x, y = event.pos
                    i = x // 32
                    j = y // 30
                    row[i][j] = 2
                    timer = 0
        # Increase timer after mouse was pressed the first time.
        if timer != 0:
            timer += dt
            # Reset after 0.5 seconds.
            if timer >= 0.5:
                print('too late')
                timer = 0

    if ter == "forest":
        for i in range(25):
            for j in range(25):
                if row[i][j] == 0:
                    win.blit(grass, (i * 32, j * 30))
                if row[i][j] == 1:
                    win.blit(tree, (i * 32, j * 30))
                if row[i][j] == 2:
                    win.blit(tree, (i * 32, j * 30))
                if row[i][j] == 3:
                    win.blit(tree, (i * 32, j * 30))    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if timer == 0:  # First mouse click.
                    timer = 0.001  # Start the timer.
                    # Set the x, y postions of the mouse click
                    x, y = event.pos
                    i = x // 32
                    j = y // 30
                    row[i][j] = 0
                    # Click again before 0.5 seconds to double click.
                elif timer < 0.5:
                    x, y = event.pos
                    i = x // 32
                    j = y // 30
                    row[i][j] = 2
                    timer = 0
        # Increase timer after mouse was pressed the first time.
        if timer != 0:
            timer += dt
            # Reset after 0.5 seconds.
            if timer >= 0.5:
                print('too late')
                timer = 0
    if ter == "desert":
        for i in range(25):
            for j in range(25):
                if row[i][j] == 0:
                    win.blit(rock2, (i * 32, j * 30))
                if row[i][j] == 1:
                    win.blit(dirt, (i * 32, j * 30))
                if row[i][j] == 2:
                    win.blit(dirt, (i * 32, j * 30))
                if row[i][j] == 3:
                    win.blit(dirt, (i * 32, j * 30))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if timer == 0:  # First mouse click.
                    timer = 0.001  # Start the timer.
                    # Set the x, y postions of the mouse click
                    x, y = event.pos
                    i = x // 32
                    j = y // 30
                    row[i][j] = 1
                    # Click again before 0.5 seconds to double click.
                elif timer < 0.5:
                    x, y = event.pos
                    i = x // 32
                    j = y // 30
                    row[i][j] = 0
                    timer = 0
        # Increase timer after mouse was pressed the first time.
        if timer != 0:
            timer += dt
            # Reset after 0.5 seconds.
            if timer >= 0.5:
                print('too late')
                timer = 0  

    if ter == "town":
        for i in range(25):
            for j in range(25):
                if row[i][j] == 0:
                    win.blit(hut, (i * 32, j * 30))
                if row[i][j] == 1:
                    win.blit(stone, (i * 32, j * 30))
                if row[i][j] == 2:
                    win.blit(tree, (i * 32, j * 30))
                if row[i][j] == 3:
                    win.blit(stone, (i * 32, j * 30))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if timer == 0:  # First mouse click.
                    timer = 0.001  # Start the timer.
                    # Set the x, y postions of the mouse click
                    x, y = event.pos
                    i = x // 32
                    j = y // 30
                    row[i][j] = 1
                    # Click again before 0.5 seconds to double click.
                elif timer < 0.5:
                    x, y = event.pos
                    i = x // 32
                    j = y // 30
                    row[i][j] = 0
                    timer = 0
        # Increase timer after mouse was pressed the first time.
        if timer != 0:
            timer += dt
            # Reset after 0.5 seconds.
            if timer >= 0.5:
                print('too late')
                timer = 0 

    if ter == "fields":
        for i in range(25):
            for j in range(25):
                if row[i][j] == 0:
                    win.blit(grass, (i * 32, j * 30))
                if row[i][j] == 1:
                    win.blit(grass, (i * 32, j * 30))
                if row[i][j] == 2:
                    win.blit(stump, (i * 32, j * 30))
                if row[i][j] == 3:
                    win.blit(grass, (i * 32, j * 30))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if timer == 0:  # First mouse click.
                    timer = 0.001  # Start the timer.
                    # Set the x, y postions of the mouse click
                    x, y = event.pos
                    i = x // 32
                    j = y // 30
                    row[i][j] = 1
                    # Click again before 0.5 seconds to double click.
                elif timer < 0.5:
                    x, y = event.pos
                    i = x // 32
                    j = y // 30
                    row[i][j] = 0
                    timer = 0
        # Increase timer after mouse was pressed the first time.
        if timer != 0:
            timer += dt
            # Reset after 0.5 seconds.
            if timer >= 0.5:
                print('too late')
                timer = 0  
    pygame.display.update()

pygame.quit()
