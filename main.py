import requests
import pygame
import random
# URL = "http://api.open-notify.org/astros.json"

# res = requests.get(URL) # get the data
# res = res.json() # convert data to Python format

# print(res)
win = pygame.display.set_mode((800, 600))
img = pygame.image.load('assets/gfx/Overworld.png').convert()

grass = pygame.Surface([32, 30]).convert()
grass.blit(img, (0, 0), (0, 145, 32, 30))
water = pygame.Surface([32, 30]).convert()
water.blit(img, (0, 0), (0, 17, 32, 30))
pit = pygame.Surface([32, 30]).convert()
pit.blit(img, (0, 0), (240, 370, 32, 30))

row = []
for j in range(25):
    tempRow = []
    for i in range(25):
        num = random.randint(0, 2)
        tempRow.append(num)
    row.append(tempRow)
    

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))

    # row = [
    #     [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2)]
    #     [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2)], 
    #     [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2)], 
    #     [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2)],
    #     [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2)],
    #     [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2)],
    #     [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2)],
    #     [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2)],
    #     [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2)],
    #     [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2)],
    #     [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2)],
    #     [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2)],
    #     [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2)],
    #     [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2)],
    #     [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2)],
    #     [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2)],
    #     [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2)],
    #     [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2)],
    #     [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2)],
    #     [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2)],
    #     [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2)],
    #     [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2)],
    #     [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2)],
    #     [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2)]
        
    # ]



    for i in range(25):
        for j in range(25):
            if row[i][j] == 0:
                win.blit(grass, (i * 32, j * 30))
            if row[i][j] == 1:
                win.blit(water, (i * 32, j * 30))
            if row[i][j] == 2:
                win.blit(pit, (i * 32, j * 30))
            

    pygame.display.update()

pygame.quit()
