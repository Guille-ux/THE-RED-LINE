import random
import pygame
import sys
import time
import math

#game constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
#game variables
move = True
on = False
select = None
target = None
#screen init
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((500, 700))
clock = pygame.time.Clock()
pygame.display.set_caption("THE RED LINE")
#graphics load
destroy = pygame.image.load("assets/destroy.png")
play = pygame.image.load("assets/play.png")
buttonrect = play.get_rect(centerx = 50)
buttonrect.x = 230
buttonrect.y = 350
tonk = pygame.image.load("assets/tonks.png")
tank = pygame.image.load("assets/tank.png")
infantry = pygame.image.load("assets/infantry.png")
block = pygame.image.load("assets/terrain.png")
blocks = []
for y in range(10):
    for x in range(7):
        blockrect = block.get_rect(left=x*70, top=y*70)
        terrain = (block, blockrect.copy())
        blocks.append(terrain)
#allies and enemys
enemys = []
for x in range(7):
    tankrect = tank.get_rect(left=x*70, top=630)
    enemys.append((tonk, tankrect, 12, 6))
allies = []
for x in range(7):
    tankrect = tank.get_rect(left=x*70, top=0)
    allies.append((tank, tankrect, 10, 5))
for x in range(7):
    peoplerect = infantry.get_rect(left=x*70, top=70)
    allies.append((infantry, peoplerect, 5, 3))


#font
font = pygame.font.Font("assets/pixel.ttf", 16)
font1 = pygame.font.Font("assets/pixel.ttf", 36)
text1 = font1.render("THE RED LINE", False, WHITE)
#functions
def draw():
    global allies
    global on
    screen.fill(BLACK)
    if on == False:
        screen.blit(text1, (200, 100))
        screen.blit(play, buttonrect)
    else:
        for pas in blocks:
            screen.blit(pas[0], pas[1])
        for allie in allies:
            screen.blit(allie[0], allie[1])
        for enemy in enemys:
            screen.blit(enemy[0], enemy[1])
while True:
    draw()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                on_mouse_down(event.pos)
    def on_mouse_down(pos):
        global on, select, allies, blocks, target, move, destroy

        if on == False:
            if buttonrect.collidepoint(pos):
                on = True
        else:
            collision = False
            if select is None:
                for allie in allies:
                    if allie[1].collidepoint(pos):
                        if allie[2] <= 0:
                            pass
                        else:
                            select = allie
                        break
            else:
                distance = math.sqrt((select[1].x - pos[0])**2 + (pos[1] - select[1].y)**2)
                if distance <= 140:
                    for enemy in enemys:
                        if enemy[1].collidepoint(pos):
                            enemy[2] -= select[3] 
                            select[2] -= enemy[3]
                            if enemy[2] <= 0:
                                enemy[0] = destroy
                            if select[2] <= 0:
                                select[0] = destroy
                        select = None
                        collision = True
                    if not collision:
                        for terr in blocks:
                            if terr[1].collidepoint(pos):
                                target = terr
                                break
                    move = True
                if target is not None:
                    select[1].center = target[1].center

                select = None
                target = None


    pygame.display.flip()
    clock.tick(60)
