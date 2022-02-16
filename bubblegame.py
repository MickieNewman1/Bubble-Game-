# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 14:19:49 2021

@author: mwnew
"""

#Bubble Game
#Mickie Newman
#20/03/05
#
#
# for this code i used the bubbles click and drag code from class and the list collision snippet from class
import pygame
from random import *

blue = (135,206,250)


pygame.init()




screen = pygame.display.set_mode((600,600))

Run = True
drag = False

x = 300 
y = 300
r = 60 
wiggleLR = 10
wiggleUD = 20
a= 100
b= 0
h= 600
w= 100
hit = False
run= True
circles = randint(1,5)


goal = pygame.Rect(a,b,h,w) #creating the goal that interacts with the circles


rectangles = [] #rectangles under the circles list
for i in range(circles):
    
    rectangles.append(pygame.Rect(x,y,r*2,r*2)) #we're setting a rectangle underneath our circle
#the r is the circle  RADIUS, but we want the rect with to be equal to DIAMETER, so:
#diameter = radius * 2


while Run: #start the game loop!
    
    for event in pygame.event.get(): #scan all events --things happening outside python (mouse and keyboard actions)
        if event.type == pygame.QUIT:
            pygame.quit() #add a quit function so it stops up background tasks
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos() #get our x and y positions of where the click happened
            for i in range(circles):
                if rectangles[i].collidepoint(pos[0],pos[1]):
                    drag = True #whenever the mouse is down, we can potentially drag our shape. Word.
                    selected = i
                    print(selected)
                    offsetX = rectangles[i].x - pos[0] #let's calculate the difference between where the rectangle is and where the click happened
                    offsetY = rectangles[i].y - pos[1]
            
        elif event.type == pygame.MOUSEMOTION:
            if drag: #remember drag is a boolean, and if statements want to know if something is true or not...so we can just pass our variable here!
                pos = event.pos #update position as mouse moves around
                #update the position of the shape based on where the mouse motion event is happening (where the cursor is)
                rectangles[selected].x = pos[0] + offsetX 
                rectangles[selected].y = pos[1] + offsetY
            
        elif event.type == pygame.MOUSEBUTTONUP: #ok, now we're done dragging, so we want to detect when the mouse button is released.
            drag = False #we can set our boolean to false, so we can't update our Rect position.
            if goal.collidelistall(rectangles): 
                hit = True
                
                
    speed = [randint(-wiggleLR,wiggleLR),randint(-wiggleUD,wiggleUD)]  # circles will wiggle
    
    screen.fill(blue) #draw/redraw the screen to "erase" previous drawings
    pygame.draw.rect(screen,(0,0,0),(a,b,w,h))
    
    #now let's draw the circle object on top of our rectangle
    
    for i in range(circles):
        pygame.draw.circle(screen, (0,0,0), (rectangles[i].x + speed[0], rectangles[i].y+speed[1]), r)
        if hit == True:
            pygame.draw.circle(screen, blue,(rectangles[i].x  + speed[0], rectangles[i].y+speed[1]), r) #turns the circles blue  
            pygame.draw.rect(screen,(0,0,0),(a,b,w,h)) #the goal covers over the circles 
                
    pygame.display.update() 
 
    
    


    

      