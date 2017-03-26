import pygame
import time
import sys
import math
import random

from pygame.locals import*
pygame.init()

#dimensional parameters
screen_width = 1200
screen_height = 700

#game window screen
screen = pygame.display.set_mode((screen_width,screen_height),0,0)
pygame.display.set_caption("Xplore")

blue = (0,189,255)
yellow = (255,253,0)
orange = (255,75,0)
red = (242,10,14)
pink = (255,0,253)
green = (3,255,0)
white=(255,255,255)

#images used
background = pygame.image.load("tankgame\\img\\gamebgfinal.jpg")
level1bg = pygame.image.load("tankgame\\img\\level1bg.jpg")
tankbase = pygame.image.load("tankgame\\img\\spaceship.png").convert_alpha()
pallette = pygame.image.load("tankgame\\img\\pallette.png").convert_alpha()
pallettebig = pygame.image.load("tankgame\\img\\pallettebig.png").convert_alpha()
planet1 = pygame.image.load("tankgame\\img\\planet1.png").convert_alpha()
planet2 = pygame.image.load("tankgame\\img\\planet2.png").convert_alpha()
planet3 = pygame.image.load("tankgame\\img\\planet3.png").convert_alpha()
explosion = pygame.image.load("tankgame\\img\\explosion.png").convert_alpha()

#astroids
astroid1 = pygame.image.load("tankgame\\img\\astroid1.png").convert_alpha()
astroid2 = pygame.image.load("tankgame\\img\\astroid2.png").convert_alpha()
astroid3 = pygame.image.load("tankgame\\img\\astroid3.png").convert_alpha()
astroid4 = pygame.image.load("tankgame\\img\\astroid4.png").convert_alpha()
astroid5 = pygame.image.load("tankgame\\img\\astroid5.png").convert_alpha()
astroid6 = pygame.image.load("tankgame\\img\\astroid6.png").convert_alpha()
astroid7 = pygame.image.load("tankgame\\img\\astroid7.png").convert_alpha()
astroid8 = pygame.image.load("tankgame\\img\\astroid8.png").convert_alpha()
astroid9 = pygame.image.load("tankgame\\img\\astroid9.png").convert_alpha()
astroidsimg = [astroid1,astroid2,astroid3,astroid4,astroid5,astroid6,astroid7,astroid8,astroid9]

def checkpos():
    mx,my = pygame.mouse.get_pos()
    return mx,my

def calc_distance(my,mx):
    dist = math.sqrt((my-screen_height/2)*(my-screen_height/2)+(mx-screen_width/2 )*(mx-screen_width/2))
    return dist

class bullet:

    def __init__(self,color,startpx,startpy,angle_radians):
        self.startpx = startpx
        self.startpy = startpy
        self.color = color
        self.angle_radians = angle_radians
        

    def move(self):
        self.startpx += 10*math.cos(self.angle_radians)
        self.startpy += 10*math.sin(self.angle_radians)
        pygame.draw.circle(screen,self.color,(int(self.startpx),int(self.startpy)),3)
        
    def give_pos(self):
        return self.startpx,self.startpy
    

        
class astroidgen:
    
    def __init__(self,startpx,startpy,img,x,y):
        self.startpx = startpx
        self.startpy = startpy
        self.x = x
        self.y = y
        self.img = img
        

    def move(self):
        self.startpx += random.randint(-10,10)
        self.startpy += random.randint(-10,10)
        screen.blit(astroidsimg[self.img],(self.x+self.startpx,self.y+self.startpy))
        
      
    def give_pos(self):
        return x+self.startpx,y+self.startpy

def main():

    #gameparametersm
    game_exit = False
    clock = pygame.time.Clock()

   

    #colors


    #parametes and contents
    x = -1000
    y = -1000
    xchange = 0
    ychange = 0
    fps = 30
    speed = 5
    change_ang = 0
    pro = 0
    on=0
    bullets = []
    color = blue
    planetposx = [50,8000,5500]
    planetposy = [50,4000,900]
    astroids = []
    bx = 0
    by = 0
    ax = 0
    ay = 0
    while not game_exit:
        
        screen.blit(background,(x,y))
        screen.blit(planet1,(x+planetposx[0],y+planetposy[0]))
        screen.blit(planet2,(x+planetposx[1],y+planetposy[1]))
        screen.blit(planet3,(x+planetposx[2],y+planetposy[2]))


        if random.randint(0,4) is 1:
            astroids.append(astroidgen(random.randint(0,12000-screen_width),random.randint(0,7000-screen_height),random.randint(0,8)),x,y)
        
        
        mousex,mousey = checkpos()
        
        distance = calc_distance(mousey,mousex)

        if distance != 0:
            xchange = -speed*(mousex-screen_width/2)/distance
            ychange = -speed*(mousey-screen_height/2)/distance
            
        x = x+xchange
        y = y+ychange

        if x > 0:
            xchange = 0
            x = 0
        if x < -12000+screen_width:
            xchange = 0
            x = -12000+screen_width
            
        if y > 0:
            ychange = 0
            y = 0

        if y < -7000+screen_height:
            ychange = 0
            y = -7000+screen_height

        angle_radians = math.atan2((mousey-screen_height/2),(mousex-screen_width/2 ))
        angle = 360 - math.degrees(angle_radians)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == K_q:
                    game_exit = True
                if event.key == K_UP:
                    change_ang += 60
                    if change_ang == 360:
                        change_ang = 0
                if event.key == K_DOWN:
                    change_ang -= 60
                    if change_ang == -360:
                        change_ang = 0
                if event.key == K_SPACE:
                    pro = 1
                    
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
               bullets.append(bullet(color,screen_width/2+50*math.cos(angle_radians),screen_height/2+50*math.sin(angle_radians),angle_radians))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                speed = 15
            if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                speed = 5
        
        tankbaserot = pygame.transform.rotate(tankbase,angle-90)
        
        if pro == 1:
            change_ang+=30
            on+=1
            color = white
            if on>=92:
                on=0
                pro=0
                change_ang = 0
            palletterot = pygame.transform.rotate(pallette,angle-90+change_ang)
        else:
             if change_ang == 0 :
                color = red
             elif change_ang == 60  or change_ang==-300:
                color = orange
             elif change_ang == 120 or change_ang==-240:
                color = yellow
             elif change_ang == 180 or change_ang==-180:
                color = blue
             elif change_ang == 240 or change_ang==-120:
                color = green
             elif change_ang == 300 or change_ang==-60:
                color = pink
             palletterot = pygame.transform.rotate(pallette,angle-90+change_ang)


        for ammo in bullets:
            ammo.move()
            bx,by = ammo.give_pos()
            if bx < 0 or bx>screen_width or by < 0 or by>screen_height:
                bullets.remove(ammo)
            
        
        rect = palletterot.get_rect(center = (screen_width/2,screen_height/2))
        screen.blit(palletterot,rect)

        rect = tankbaserot.get_rect(center = (screen_width/2,screen_height/2))
        screen.blit(tankbaserot,rect)

        for ast in astroids:
            ast.move()

        for ast in astroids:
            ax,ay = ast.give_pos()
            for ammo in bullets:
                bx,by = ammo.give_pos()
                if bx>=ax and bx<=ax+50:
                   if by>=ay and by<=ay+50:
                       astroids.remove(ast)
                       bullets.remove(ammo)
                       screen.blit(explosion,(ax,ay),(0,0,50,50))
                   
        pygame.display.update()
        clock.tick(fps)
main()

pygame.quit()
sys.exit()
quit()
