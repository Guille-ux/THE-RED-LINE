# Game created by Guille-ux and Nunte :D

import random
import pygame
import sys
import time
import math
import ctypes

# windows taskbar icon thingy
myappid = 'guilleux.pythongame.theredline.idk' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

#game constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
#game variables
info = False
move = True
on = False
win = False
lose = False
select = None
target = None
laser = 0
ot = time.time()
#game init
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("sfx/music.mp3")
pygame.mixer.music.play(-1)
screen = pygame.display.set_mode((500, 700))
clock = pygame.time.Clock()
pygame.display.set_caption("THE RED LINE")
#graphics load
antitank = pygame.image.load("assets/antitank.png")
fond = pygame.image.load("assets/startbg.png")
antitankn = pygame.image.load("assets/antitankn.png")
destroy = pygame.image.load("assets/destroy.png")
play = pygame.image.load("assets/play.png")
icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)
2but = pygame.imgae.load("assets/INFO.png")
2but_rect = 2but.get_rect(centerx = 50)
2but_rect.x = 200
2but_rect.y = 400
3but = pygame.imgae.load("assets/back.png")
3but_rect = 3but.get_rect(centerx = 50)
3but_rect.x = 20
3but_rect.y = 20
buttonrect = play.get_rect(centerx = 50)
buttonrect.x = 200
buttonrect.y = 300
kv = pygame.image.load("assets/kv-2.png")
n4z1s = pygame.image.load("assets/n4z1s.png")
tonk = pygame.image.load("assets/tonks.png")
tank = pygame.image.load("assets/tank.png")
tiger = pygame.image.load("assets/tiger.png")
infantry = pygame.image.load("assets/infantry.png")
block = pygame.image.load("assets/terrain.png")
blocks = []
for y in range(10):
    for x in range(7):
        blockrect = block.get_rect(left=x*70, top=y*70)
        terrain = (block, blockrect.copy())
        blocks.append(terrain)
#font
font = pygame.font.Font("assets/pixel.ttf", 16)
font1 = pygame.font.Font("assets/pixel.ttf", 36)
text1 = font1.render("THE RED LINE", False, BLACK)
text2 = font1.render("[=WIN=]", False, BLACK)
text3 = font1.render("[=LOSE=]", False, BLACK)
#functions
def prep():
    global enemys
    global allies
    enemys = []
    for x in range(7):
        tankrect = tank.get_rect(left=x*70, top=630)
        if x % 2 == 0:
            enemys.append([tonk, tankrect, 11, 5.5, "attack"])
        else:
            enemys.append([tiger, tankrect, 16, 10.5, "attack"])
    for x in range(7):
        tankrect = tank.get_rect(left=x*70, top=560)
        if x % 2 == 0:
            enemys.append([n4z1s, tankrect, 5, 3, "defend"])
        else:
            enemys.append([antitankn, tankrect, 7, 4, "defend"])
    allies = []
    for x in range(7):
        tankrect = tank.get_rect(left=x*70, top=0)
        if x % 2 == 0:
            allies.append([tank, tankrect, 10, 5, "attack"])
        else:
            allies.append([kv, tankrect, 15, 10, "attack"])
    for x in range(7):
        peoplerect = infantry.get_rect(left=x*70, top=70)
        if x % 2 == 0:
            allies.append([infantry, peoplerect, 5, 3.5, "defend"])
        else:
            allies.append([antitank, peoplerect, 7, 4, "defend"])

def draw():
    global allies
    global on
    global win
    global lose
    screen.fill(BLACK)
    if on == False and win == False and lose == False:
        screen.blit(fond, 0, 0)
        screen.blit(3but, 3but_rect)
    if on == False and win == False and lose == False:
        screen.blit(fond, (0, 0))
        screen.blit(text1, (130, 100))
        screen.blit(play, buttonrect)
        screen.blit(2but, 2but_rect)
    if on == False and win == True:
        screen.blit(fond, (0, 0))
        screen.blit(text1, (130, 100))
        screen.blit(play, buttonrect)
        screen.blit(text2, (180, 200))
        screen.blit(2but, 2but_rect)
    if on == False and lose == True:
        screen.blit(fond, (0, 0))
        screen.blit(text1, (130, 100))
        screen.blit(play, buttonrect)
        screen.blit(text3, (180, 200))
        screen.blit(2but, 2but_rect)     
    elif on == True and win == False and lose == False:
        for pas in blocks:
            screen.blit(pas[0], pas[1])
        for allie in allies:
            screen.blit(allie[0], allie[1])
        for enemy in enemys:
            screen.blit(enemy[0], enemy[1])
while True:
    if on == True:
        lose = True
        for allie in allies:
            if allie[2] == 0:
                allie = destroy
            if allie[2] > 0:
                lose = False
        win = True
        for ene in enemys:
            if ene[2] == 0:
                ene[0] = destroy
            if ene[2] > 0:
                win = False
    else:
        ot = 0
    if win == True:
        on = False
    if lose == True:
        on = False
    draw()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                on_mouse_down(event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for all in allies:
                    all[2] = 0
                    all[0] = destroy
    def on_mouse_down(pos):
        global on, select, allies, blocks, target, move, destroy, laser, ot
        if on == False an info == False:
            if buttonrect.collidepoint(pos):
                on = True
                win = False
                lose = False
                prep()
        elif on == False and info == True:
            if 3but_rect.collidepoint(pos):
                info = False
        else:
            collision = False
            if select is None:
                for allie in allies:
                    if allie[1].collidepoint(pos):
                        if allie[2] == 0:
                            pass
                        else:
                            select = allie
                        break
            else:
                abonus = 1
                ebonus = 1
                distance = math.sqrt((select[1].x - pos[0])**2 + (pos[1] - select[1].y)**2)
                if distance <= 140:
                    for enemy in enemys:
                        if enemy[1].collidepoint(pos) and enemy[2] > 0:
                            if select[0] == "assets/antitank.png" and enemy[0] == "assets/tonks.png":
                                abonus += 0.25
                            elif select[0] == "assets/tank.png" and enemy[0] == "assets/antitankn.png":
                                ebonus += 0.25
                            elif select[0] == "assets/tank.png" and enemy[0] == "assets/tonks.png":
                                abonus += 0.25
                                ebonus += 0.25
                            elif select[0] == "assets/infantry.png" and enemy[0] == "assets/n4z1s.png":
                                abonus += 0.25
                                ebonus += 0.25
                            elif select[0] == "assets/infantry.png" and enemy[0] == "assets/antitankn.png":
                                abonus += 1
                            elif select[0] == "assets/antitank.png" and enemy[0] == "assets/n4z1s.png":
                                ebonus += 1
                            elif select[0] == "assets/kv-2.png" and enemy[0] == "assets/tonks.png":
                                abonus += 0.50
                            elif select[0] == "assets/tank.png" and enemy[0] == "assets/tiger.png":
                                ebonus += 0.50
                            elif select[0] == "assets/antitank.png" and enemy[0] == "assets/tiger.png":
                                abonus += 1.25
                            elif select[0] == "assets/kv-2.png" and enemy[0] "assets/antitankn.png":
                                ebonus += 1.25
                            if select[4] == "attack":
                                abonus += 0.50
                            enemy[2] -= select[3] * abonus
                            if enemy[4] == "defend":
                                ebonus += 0.50
                            select[2] -= enemy[3] * ebonus
                            if enemy[2] < select[2]:
                                enemy[2] = 0
                                enemy[0] = destroy
                                break
                            elif enemy[2] > select[2]:
                                select[2] = 0
                                select[0] = destroy
                                break
                            else:
                                enemy[2], enemy[3] = 0, 0
                                enemy[0] = destroy
                                select[2], select[3] = 0, 0
                                select[0] = destroy
                                break

                    abonus = 1
                    ebonus = 1
                    for terr in blocks:
                        if terr[1].collidepoint(pos):
                            target = terr
                            break
                    move = True
                if target is not None:
                    select[1].center = target[1].center
                lose = True
                for allie in allies:
                    if allie[2] == 0:
                        pass
                    else:
                        lose = False
                        break
                win = True
                for ene in enemys:
                    if ene[2] == 0:
                        pass
                    else:
                        win = False
                        break
                target = None
                algo = False
                for ene in enemys:
                    if ene[2] > 0:
                        for all in allies:
                            distance = math.sqrt((ene[1].x - all[1].x)**2 + (all[1].y - ene[1].y)**2)
                            if distance <= 140 and all[2] > 0:
                                ene[1].center = all[1].center
                                if all[1].colliderect(ene[1]):
                                    if all[0] == "assets/antitank.png" and ene[0] == "assets/tonks.png":
                                        abonus += 0.25
                                    elif all[0] == "assets/tank.png" and ene[0] == "assets/antitankn.png":
                                        ebonus += 0.25
                                    elif all[0] == "assets/tank.png" and ene[0] == "assets/tonks.png":
                                        abonus += 0.25
                                        ebonus += 0.25
                                    elif all[0] == "assets/infantry.png" and ene[0] == "assets/n4z1s.png":
                                        abonus += 0.25
                                        ebonus += 0.25
                                    elif all[0] == "assets/infantry.png" and ene[0] == "assets/antitankn.png":
                                        abonus += 1
                                    elif all[0] == "assets/antitank.png" and ene[0] == "assets/n4z1s.png":
                                        ebonus += 1
                                    elif all[0] == "assets/kv-2.png" and enemy[0] == "assets/tonks.png":
                                        abonus += 0.50
                                    elif all[0] == "assets/tank.png" and ene[0] == "assets/tiger.png":
                                        ebonus += 0.50
                                    elif select[0] == "assets/antitank.png" and enemy[0] == "assets/tiger.png":
                                        abonus += 1.25
                                    elif all[0] == "assets/kv-2.png" and ene[0] "assets/antitankn.png":
                                        ebonus += 1.25
                                    if all[4] == "defend":
                                        abonus += 0.50
                                    if ene[4] == "attack":
                                        ebonus += 0.50
                                    all[2] -= ene[3] * ebonus
                                    ene[2] -= all[3] * abonus
                                    if ene[2] < all[2]:
                                        ene[2] = 0
                                        ene[0] = destroy
                                        break
                                    elif ene[2] > all[2]:
                                        all[2] = 0
                                        all[0] = destroy
                                        break
                                    else:
                                        ene[2], ene[3] = 0, 0
                                        ene[0] = destroy
                                        all[2], all[3] = 0, 0
                                        all[0] = destroy
                                        break
                    break
                for en in range(len(enemys)):
                    ene = enemys[(en + laser) % len(enemys)]
                    if ene[2] > 0:
                        pass
                    else:
                        ene = None
                laser += 1
                if not algo and ene != None:
                    if not ene[1].top == 0:
                        ene[1].top -= 70
                    else:
                        ene[1].top += 70
                    for all in allies:
                         if all[1].colliderect(ene[1]):
                             if all[0] == "assets/antitank.png" and ene[0] == "assets/tonks.png":
                                 abonus += 0.25
                             elif all[0] == "assets/tank.png" and ene[0] == "assets/antitankn.png":
                                 ebonus += 0.25
                             elif all[0] == "assets/tank.png" and ene[0] == "assets/tonks.png":
                                 abonus += 0.25
                                 ebonus += 0.25
                             elif all[0] == "assets/infantry.png" and ene[0] == "assets/n4z1s.png":
                                 abonus += 0.25
                                 ebonus += 0.25
                             elif select[0] == "assets/infantry.png" and enemy[0] == "assets/antitankn.png":
                                 abonus += 1
                              elif all[0] == "assets/antitank.png" and ene[0] == "assets/n4z1s.png":
                                 ebonus += 1
                             elif all[0] == "assets/kv-2.png" and enemy[0] == "assets/tonks.png":
                                 abonus += 0.50
                             elif all[0] == "assets/tank.png" and ene[0] == "assets/tiger.png":
                                 ebonus += 0.50
                             elif select[0] == "assets/antitank.png" and enemy[0] == "assets/tiger.png":
                                 abonus += 1.25
                             elif all[0] == "assets/kv-2.png" and ene[0] "assets/antitankn.png":
                                 ebonus += 1.25
                                 ebonus += 1
                             if all[4] == "defend":
                                 abonus += 0.50
                             if ene[4] == "attack":
                                 ebonus += 0.50
                                 all[2] -= ene[3] * ebonus
                                 ene[2] -= all[3] * abonus
                             if ene[2] < all[2]:
                                 ene[2] = 0
                                 ene[0] = destroy
                             elif ene[2] > all[2]:
                                 all[2] = 0
                                 all[0] = destroy
                             else:
                                 ene[2], ene[3] = 0, 0
                                 ene[0] = destroy
                                 all[2], all[3] = 0, 0
                                 all[0] = destroy

                else:
                    win = True
                select = None
    clock.tick(60)
    pygame.display.flip()
