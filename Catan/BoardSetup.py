import math
import pygame
import random
import sys
from pygame.draw import polygon
from pygame.locals import *


# Initialized the game engine
pygame.init()

# Initialized some game colors
backGround = (0,171,255)

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
#class House():
#class City():
#class TileValue?():        
       

# Attemp to setup entire board
boardSetup(center, size)


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
                

    # Update the display
    pygame.display.flip()
    
pygame.quit()
sys.exit()