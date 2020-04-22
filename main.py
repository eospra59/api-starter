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
rock = pygame.Surface([32, 30]).convert()
rock.blit(caveimg, (0, 0), (145, 115, 32, 30))
tree = pygame.Surface([32, 30]).convert()
tree.blit(treeimg, (0, 0), (190, 190, 32, 30))

row = []
for j in range(25):
    tempRow = []
    for i in range(25):
        num = random.randint(0, 2)
        tempRow.append(num)
    row.append(tempRow)
    
ter = input("What type of terrain would you like?")

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

    if ter == "forest":
        for i in range(25):
            for j in range(25):
                if row[i][j] == 0:
                    win.blit(grass, (i * 32, j * 30))
                if row[i][j] == 1:
                    win.blit(tree, (i * 32, j * 30))
                if row[i][j] == 2:
                    win.blit(tree, (i * 32, j * 30))        

    pygame.display.update()

pygame.quit()
