import math
from re import X
import pygame
import random
import sys
from pygame.draw import polygon
from pygame.locals import *


# Initialized the game engine
pygame.init()

# Initialized some game colors
backGround = (0,171,255)  #blue
WHITE = (255,255,255) #white

# Tile Colors
brickColor = (150,75,0)
hayColor = (236,204,162)
stoneColor = (128,128,128)
sheepColor = (144,238,144)
woodColor = (1,50,32)
blackColor = (0,0,0)

# Creates a list to store all of the tile colors
tileColorList = [brickColor,hayColor,stoneColor,sheepColor,woodColor]

# Create a window and set resolution
window = pygame.display.set_mode((900,900))

# Fill the screen with a 'background' color
window.fill(backGround)

# Set fps to 60
FPS = pygame.time.Clock()
FPS.tick(60)

# Center decides on where the first hexagon is placed
center = (200,100)
size = 75

# Function to calculate hexagon points
def hexagon_points(center, size):
    points = []
    for i in range(6):
        angle_deg = 60 * i - 30
        angle_rad = math.radians(angle_deg)
        x = center[0] + size * math.cos(angle_rad)
        y = center[1] + size * math.sin(angle_rad)
        points.append((x, y))
    return points

# Function to draw a hexagon
def draw_hexagon(center, size):
    points = hexagon_points(center, size)
    pygame.draw.polygon(window, blackColor, points,3)
    pygame.draw.polygon(window, random.choice(tileColorList), points)
   


# ------------------- Draws a hexagon in ceratain directions -----------------------
# Direction is based off of the center, which are passed in as coords (tuple) of another hexagon 
def hexUpLeft(center,size):
    newCenter = (center[0] - .86 * size, center[1] - 1.5 * size)
    return newCenter

def hexUpRight(center,size):
    newCenter = (center[0] + .86 * size, center[1] - 1.5 * size)
    return newCenter

def hexDownLeft(center,size):
    newCenter = (center[0] - .86 * size, center[1] + 1.5 * size)
    return newCenter

def hexDownRight(center,size):
    newCenter = (center[0] + .86 * size, center[1] + 1.5 * size)
    return newCenter

def hexRight(center,size):
    newCenter = (center[0] + 1.73 * size, center[1])
    return newCenter

def hexLeft(center,size):
    newCenter = (center[0] - 1.73 * size, center[1])
    return newCenter  

def boardSetup(center, size):
    
    # ---- Start of Draing ----
    draw_hexagon(center,size)
    temp = center
    
    for i in range(0,2):
        temp = hexRight(temp,size)
        draw_hexagon(temp,size)
    
    # ------------ Top 3 Hexagons ---------------------
    temp = hexDownRight(temp, size)
    draw_hexagon(temp,size)
    
    for i in range(0,3):
        temp = hexLeft(temp,size)
        draw_hexagon(temp,size)
    
    # ------------- 2nd Row of Hexagons --------------------
    temp = hexDownLeft(temp,size)
    draw_hexagon(temp,size)
    
    for i in range(0,4):
        temp = hexRight(temp,size)
        draw_hexagon(temp,size)
        
    # -------------- 3rd Row of Hexagons -------------------
    temp = hexDownLeft(temp, size)
    draw_hexagon(temp,size)
    
    for i in range(0,3):
        temp = hexLeft(temp,size)
        draw_hexagon(temp,size)
     
    # -------------- Last Row of Hexagons -------------------
    temp = hexDownRight(temp, size)
    draw_hexagon(temp,size)
    
    for i in range(0,2):
        temp = hexRight(temp,size)
        draw_hexagon(temp,size)
    
    
    
# ---- Will make the game objects classes soon ----
        
#class Board():
    #def __init__self(self):
        #self.rect = self.
        
#class Road():
class House():
    def __init__(self,x,y,w,h,id):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h
        
        self.w = w
        self.h = h
        
        self.fillColor = WHITE
        self.stained = False
        self.id = id
        
    # Setting the new position of a rectangle to mouse position
    def setXY(self,xy):
        self.x1,self.y1 = xy
        self.x2 = xy[0] + self.w
        self.y2 = xy[1] + self.h
        
    # Returns a coordinate
    def getXY(self):
        return(self.x1,self.y1)
    
    # Returns values needed to build a rectangle in the form of a tuple
    def rect(self):
        # The following 3 lines update the rectangle coords 
        # Now it will be placed 0.5 * width and 0.5 * height 
        # This centers the house on the mouse, so where ever you click is more accurate
        coords = self.getXY()
        x1 = coords[0] - (0.5*self.w)
        y1 = coords[1] - (0.5*self.h)
        
        return (x1,y1,self.w, self.h)
    
    # Returns values needed to test for colision (x1,y1,x2,y2) in the form of a tuple
    def coords(self):
        return self.getXY() + (self.x2, self.y2)
    
    def draw(self, surface = None):
        if not surface:
            surface = pygame.display.get_surface()
        pygame.draw.rect(surface,self.fillColor,self.rect(),0)
        

#class City():
#class TileValue?():        
       

# Attempt to setup entire board
boardSetup(center, size)

# Attempt to setup a single house and test for colision
house = House(100,100,25,25,0)
house.draw(window)


# ------------------------------ Game loop begins ------------------------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # Allows user to hit ESCAPE to exit the game window
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
    # Placeing a house by getting mouse position and leftclicking
    mb = pygame.mouse.get_pressed()
    
    house.setXY(pygame.mouse.get_pos())
    if mb[0]:
        house.draw(window)
    
    # Update the display
    pygame.display.flip()
    
pygame.quit()
sys.exit()