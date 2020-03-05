import requests
import pygame
# URL = "http://api.open-notify.org/astros.json"

# res = requests.get(URL) # get the data
# res = res.json() # convert data to Python format

# print(res)
win = pygame.display.set_mode((800, 600))
img = pygame.image.load('assets/gfx/Overworld.png').convert()

grass = pygame.Surface([25, 25]).convert()
grass.blit(img, (0, 0), (10, 200, 25, 25))
water = pygame.Surface([25, 25]).convert()
water.blit(img, (0, 0), (0, 0, 25, 25))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))
    win.blit(grass, (0, 0))
    win.blit(water, (16, 0))

    pygame.display.update()

pygame.quit()
