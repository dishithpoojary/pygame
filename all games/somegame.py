import pygame
import time
import sys
import random

from pygame.locals import*
pygame.init()

                            #PARAMETERS DECLARATION#

#dimensional parameters
screen_width = 800
screen_height = 600
babywidth = 130
babyheight = 80

#game window screen
screen = pygame.display.set_mode((screen_width,screen_height),0,32)
pygame.display.set_caption("Some Game")

#game working parameters
game_exit = False
clock=pygame.time.Clock()
fps = 30
fishx = 20
fishy = 20
fishmovex = 0
fishmovey = 0
speed = 10
eat = False
spikex = []
spikey = []
startspike = 0
babyx , babyy = 600,300
explosion_flow = 0
baby_alive = True
explosion_complete = False
blast = False
bodypart = 0
partsout = 0
babymove = 5
babydir = 1
partsgenerate = True

#colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)


#image_path
game_background = "game_images\\gamebackground.png"
fish_open_mouth = "game_images\\fishmouthopen.png"
fish_mid_mouth = "game_images\\fishmouthmid.png"
fish_close_mouth = "game_images\\fishmouthclose.png"
spike_ball = "game_images\\spike.png"
babyimage = "game_images\\baby.png"
##netopenimage = "game_images\\netopen.png"
##netopencoverimage = "game_images\\netopencover.png"
explosion1image = "game_images\\explosion1.png"
explosion2image = "game_images\\explosion2.png"
explosion3image = "game_images\\explosion3.png"
babypart1image = "game_images\\babyhand1.png"
babypart2image = "game_images\\babyleg1.png"
babypart3image = "game_images\\babyhead.png"
babypart4image = "game_images\\babyleg2.png"
babypart5image = "game_images\\babytummy.png"

#images
background = pygame.image.load(game_background).convert_alpha()
fishopen = pygame.image.load(fish_open_mouth).convert_alpha()
fishmid = pygame.image.load(fish_mid_mouth).convert_alpha()
fishclose = pygame.image.load(fish_close_mouth).convert_alpha()
spike = pygame.image.load(spike_ball).convert_alpha()
baby = pygame.image.load(babyimage).convert_alpha()
##netopen = pygame.image.load(netopenimage).convert_alpha()
##netopencover = pygame.image.load(netopencoverimage).convert_alpha()
explosion1 = pygame.image.load(explosion1image).convert_alpha()
explosion2 = pygame.image.load(explosion2image).convert_alpha()
explosion3 = pygame.image.load(explosion3image).convert_alpha()
babypart1 = pygame.image.load(babypart1image).convert_alpha()
babypart2 = pygame.image.load(babypart2image).convert_alpha()
babypart3 = pygame.image.load(babypart3image).convert_alpha()
babypart4 = pygame.image.load(babypart4image).convert_alpha()
babypart5 = pygame.image.load(babypart5image).convert_alpha()


#temporary parameters used
traverse = 0

#game logic parameters
fishmouth = [fishopen,fishmid,fishclose]
explosionlist = [explosion1,explosion2,explosion3]
bodyparts = [babypart1,babypart2,babypart3,babypart4,babypart5]


                          #gameloop
while not game_exit:
    screen.blit(background,(0,0))

    if baby_alive:
        screen.blit(baby,(babyx,babyy))

##    screen.blit(netopen,(400,300))
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                fishmovex = -speed
                fishmovey = 0
            if event.key == K_RIGHT:
                fishmovex = speed
                fishmovey = 0
            if event.key == K_UP:
                fishmovey = -speed
                fishmovex = 0
            if event.key == K_DOWN:
                fishmovey = speed
                fishmmovey = 0
            if event.key == K_SPACE:
                eat = True
                spikex.append(fishx+100)
                spikey.append(fishy+25)
                
        elif event.type == pygame.KEYUP:
                fishmovex=0
                fishmovey=0

    fishx+= fishmovex
    fishy+= fishmovey
    
    if fishx < 0:
        fishx = 0
    if fishx > screen_width-140:
        fishx = screen_width-140
    if fishy < 0:
        fishy = 0
    if fishy > screen_height-80:
        fishy = screen_height-80 

    if eat is True:
        screen.blit(fishmouth[traverse],(fishx,fishy))
        traverse = traverse+1

        if traverse > 2:
            traverse = 0
            eat = False
    else:     
        screen.blit(fishmouth[2],(fishx,fishy))

##    screen.blit(netopencover,(400,300))

    if babyy <= 10 or babyy >= screen_height-babyheight:
        babydir = babydir*-1

    babyy = babyy + babymove*babydir

    
    for spikemove in range(startspike,len(spikex)):
        screen.blit(spike,(spikex[spikemove],spikey[spikemove]))
        spike = pygame.transform.rotate(spike,90) 
        spikex[spikemove]+= speed

        if spikex[spikemove] >=babyx and spikex[spikemove] <= babyx+babywidth and baby_alive :
            if spikey[spikemove] >=babyy and spikey[spikemove] <=babyy+babyheight:
                    blast = True
                    if explosion_complete:
                        baby_alive = False    
                    screen.blit(explosionlist[explosion_flow],(babyx,babyy))
                    explosion_flow+=1
                    
                    if explosion_flow >2:
                        explosion_flow = 0
                        explosion_complete = True

        if spikex[spikemove]>800:
            startspike+= 1

    if blast is True:
        if partsgenerate is True:
            bodypartsx = [babyx-20,babyx-10,babyx,babyx+20,babyx]
            bodypartsy = [babyy+30,babyy+60,babyy,babyy+70,babyy+20]
            partsgenerate = False

        for bodypart in range(0,len(bodypartsx)):
            increment = random.randrange(0,9)
            print(increment)

            if bodypart is 0 or bodypart is 2:
                if increment%2 is 0:
                   bodypartsy[bodypart]-= 2
                   bodyparts[bodypart] = pygame.transform.rotate(bodyparts[bodypart],0)
                else :
                    bodypartsx[bodypart]-= 5
                    if increment is 3 or increment is 7:
                        bodyparts[bodypart] = pygame.transform.rotate(bodyparts[bodypart],90)      
            else :
                if increment%2 is 0:
                    bodypartsy[bodypart]+= 2
                    bodyparts[bodypart] = pygame.transform.rotate(bodyparts[bodypart],0)
                else :
                    bodypartsx[bodypart]-= 5
                    if increment is 3 or increment is 7:
                        bodyparts[bodypart] = pygame.transform.rotate(bodyparts[bodypart],90)        
            screen.blit(bodyparts[bodypart],(bodypartsx[bodypart],bodypartsy[bodypart])) 
            if bodypartsx[bodypart] < -20:
                if bodypartsy[bodypart] < -20 or bodypartsy[bodypart] > 620:
                    partsout+=1
        
        if partsout is 5:
            blast = False
            partsgenerate = True
            baby_alive = True
            partsout = False
            bodypartsx = [babyx-20,babyx-10,babyx,babyx+20,babyx]
            bodypartsy = [babyy+30,babyy+60,babyy,babyy+70,babyy+20]

    pygame.display.update();
    clock.tick(fps)





#game exit
pygame.quit()
sys.exit()
quit()
