import pygame
import time
import sys
import math

from pygame.locals import*
pygame.init()

#dimensional parameters
screen_width = 800
screen_height = 600

#game window screen
screen = pygame.display.set_mode((screen_width,screen_height),0,32)
pygame.display.set_caption("snakinator")

#gameparametersm
game_exit = False
clock = pygame.time.Clock()

#images path
backgroundpath = "snakegame_images\\gamebgfinal.jpg"
bodypath = "snakegame_images\\snakebody.png"
headpath = "snakegame_images\\snakehead.png"

#images used
background = pygame.image.load(backgroundpath)
body = pygame.image.load(bodypath).convert_alpha()
head = pygame.image.load(headpath).convert_alpha()

#parametes and contents
x = -4000
y = -3000
xchange = 0
ychange = 0
fps = 30
speed = 10
snake = [head,body,body,body,body,body,body,body]
posx = [0,0,0,0,0,0,0,0]
posy = [0,0,0,0,0,0,0,0]
angles = [0,0,0,0,0,0,0,0]
snake_len = 6
inc = 25
i=2
white=(255,255,255);


def checkpos():
    mx,my = pygame.mouse.get_pos()
    return mx,my

def calc_distance(my,mx):
    dist = math.sqrt((my-300)*(my-300)+(mx-400)*(mx-400))
    return dist

while not game_exit:
    screen.blit(background,(x,y))
    
    
    mousex,mousey = checkpos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == K_q:
                game_exit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            speed = 20
        if event.type == pygame.MOUSEBUTTONUP:
            speed = 10
            
    distance = calc_distance(mousey,mousex)

    xchange = -speed*(mousex-400)/distance
    ychange = -speed*(mousey-300)/distance
    
    x = x+xchange
    y = y+ychange

    if x > 0:
        xchange = 0
        x = 0
    if x < -7000:
        xchange = 0
        x = -7000
        
    if y > 0:
        ychange = 0
        y = 0

    if y < -5000:
        ychange = 0
        y = -5000

    angle_radians = math.atan2((mousey-300),(mousex-400))
    angle = 360 - math.degrees(angle_radians)

    angles[0] = angle_radians
    angles[1] = angle_radians
    
    headrot = pygame.transform.rotate(head,angle-90)
    bodyrot = pygame.transform.rotate(body,angle-90)
    
    posx[1] = -50*math.cos(angle_radians)
    posy[1] = -50*math.sin(angle_radians)

    angles[i] = angles[i-1]
    i+=1
    if i is snake_len+2:
        i = 2

    snake[0] = headrot
    snake[1] = bodyrot
    
    for pos in  range(2,snake_len+2):
        posx[pos] = -(50+inc)*math.cos(angles[pos])
        posy[pos] = -(50+inc)*math.sin(angles[pos])
        inc+= 25
    inc = 25

    for part in range(2,snake_len+2):
        bodyrot = pygame.transform.rotate(body,270-math.degrees(angles[part]))
        snake[part] = bodyrot
        

    for parts in range(0,snake_len+2):
        rect = snake[parts].get_rect(center = (400+posx[parts],300+posy[parts]))
        screen.blit(snake[parts],rect)
        
    
    pygame.display.update()
    clock.tick(fps)
 


pygame.quit()
print(posx,posy,angles)
sys.exit()
quit()
