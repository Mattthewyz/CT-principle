import pygame
from pygame.locals import *
import pygame.freetype
from sys import exit
import math
import random
import time
pygame.init()
screen = pygame.display.set_mode((1200,720),0,32)
th=0
v=0.5
ths=0.5006547124
class rect:
    def __init__(self,pos,w,h):
        self.pos = pos
        self.w=w
        self.h=h
        
test1=rect((300,280),10,10)
test2=rect((380,300),10,50)
test3=rect((183,250),30,70)
my_screen=[]
items=[]
my_image=[]
my_image_all=[]

flag = 0
nx = 0
ny =0
run = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.fill((255,255,255))
    x,y = pygame.mouse.get_pos()
    if '(1, 0, 0)' in str(event):
        if flag == 0:
            nx=x
            ny=y
            flag = 1
        pygame.draw.rect(screen,[0,0,0],[nx,ny,x-nx,y-ny],1)
    else:
        if flag==1:
            items.append(rect((nx,ny),x-nx,y-ny))
            flag = 0
            nx=0
            ny=0
    if '(0, 0, 1)' in str(event):
        run=1
    pygame.draw.line(screen,(0,0,0),(50,50),(50,550),2 )
    pygame.draw.line(screen,(0,0,0),(50,550),(550,550),2 )
    pygame.draw.line(screen,(0,0,0),(50,50),(550,50),2 )
    pygame.draw.line(screen,(0,0,0),(550,50),(550,550),2 )
    pygame.draw.circle(screen,(100,100,100),(300,300),250,1)

    pygame.draw.line(screen,(0,0,0),(300+250*math.cos(th-ths),300-250*math.sin(th-ths)),(300+250*math.cos(th+ths),300-250*math.sin(th+ths)),2 )
    pygame.draw.line(screen,(0,0,0),(300+250*math.cos(th-ths+math.pi),300-250*math.sin(th-ths+math.pi)),(300+250*math.cos(th+ths+math.pi),300-250*math.sin(th+ths+math.pi)),2 )

    vx=-v*math.cos(th)
    vy=v*math.sin(th)
    my_screen=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    if run == 0:
        for item in items:
            pygame.draw.rect(screen,[0,0,0],[item.pos[0],item.pos[1],item.w,item.h],1)
        pygame.display.update()
        continue

    
    for i in range(240):
        pos_light=[300+250*math.cos(th-ths)+i*(-math.sin(th)),300-250*math.sin(th-ths)+i*(-math.cos(th))]
        new_pos=[300+250*math.cos(th-ths)+i*(-math.sin(th)),300-250*math.sin(th-ths)+i*(-math.cos(th))]
        
        for item in items:
            new_pos=[300+250*math.cos(th-ths)+i*(-math.sin(th)),300-250*math.sin(th-ths)+i*(-math.cos(th))]
            while (new_pos[0]-pos_light[0])**2+(new_pos[1]-pos_light[1])**2<234256:
                #print((new_pos[0]-pos_light[0])**2+(new_pos[1]-pos_light[1])**2)
                #pygame.draw.rect(screen,[0,0,0],[new_pos[0],new_pos[1],1,1],1)
                if new_pos[0]<item.pos[0]+item.w and new_pos[0]>item.pos[0] and new_pos[1]<item.pos[1]+item.h and new_pos[1]>item.pos[1]:
                    my_screen[i]=my_screen[i]+1
                    #pygame.draw.rect(screen,[0,0,0],[new_pos[0],new_pos[1],1,1],1)
                new_pos[0]+=vx
                new_pos[1]+=vy

    pygame.draw.circle(screen,(0,0,0,50),(900,300),250,0)

    #surface = pygame.Surface((1200,720), pygame.SRCALPHA) 
    for i in range(240):
        
        l=my_screen[i]
        #pygame.draw.line(surface,(5*l,5*l,5*l),(900+250*math.cos(th-ths)-i*math.sin(th),300-250*math.sin(th-ths)-i*math.cos(th)),(900-250*math.sin(math.pi/2-th-ths)-i*math.sin(th),300+250*math.cos(math.pi/2-th-ths)-i*math.cos(th)),1)
        
        my_image.append([l,(900+242*math.cos(th-ths)-i*math.sin(th),300-242*math.sin(th-ths)-i*math.cos(th)),(900-242*math.sin(math.pi/2-th-ths)-i*math.sin(th),300+242*math.cos(math.pi/2-th-ths)-i*math.cos(th))])
        #screen.blit(surface, (0,0))
    my_image_all.append(my_image)
    my_image = []
    for t in my_image_all:
        surface = pygame.Surface((1200,720), pygame.SRCALPHA)
        #pygame.draw.circle(screen,(0,0,0,1),(900,300),250,0)
        for image in t:
            pygame.draw.line(surface,(255,255,255,image[0]/30),image[1],image[2],1)
        screen.blit(surface,(0,0))


        
#    for i in range(240):
#        pygame.draw.rect(screen,[0,0,0],[600+i,50,1,my_screen[i]],1)
                      
    for item in items:
        pygame.draw.rect(screen,[0,0,0],[item.pos[0],item.pos[1],item.w,item.h],1)

    if len(my_image_all)>50:
        my_image_all=my_image_all[1:]
#    for image in my_image:
#        pygame.draw.line(surface,(5*image[0],5*image[0],5*image[0],10),image[1],image[2],1)

    
    th+=6.28/100
    
    
    
    pygame.display.update()
    
