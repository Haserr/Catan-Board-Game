import math
import pygame
import random
import sys
from pygame.draw import polygon
from pygame.locals import *


# Initialized the game engine
pygame.init()

# Initialized some game colors
brickColor = (150,75,0)
hayColor = (236,204,162)
stoneColor = (128,128,128)
sheepColor = (144,238,144)
woodColor = (1,50,32)
blackColor = (0,0,0)

backGround = (0,171,255)

# Create a window and set resolution
window = pygame.display.set_mode((900,900))

# Fill the scree with white color
window.fill(backGround)

# Set fps to 60
FPS = pygame.time.Clock()
FPS.tick(60)



colorList = [brickColor,hayColor,stoneColor,sheepColor,woodColor]

objectColor = pygame.Color(255,0,0)
object1 = pygame.Rect((20, 50), (50, 100))

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
    pygame.draw.polygon(window, random.choice(colorList), points)
   
'''def multi_hex_coords(center,size, offset):
    if offset %4 == 0:
        newCenter = (center[0] + .86 * size, center[1] + 1.5 * size)
        return newCenter
    if offset %4 == 1:
        newCenter = (center[0] + .86 * size, center[1] - 1.5 * size)
        return newCenter
    if offset %4 == 2:
        newCenter = (center[0] - .86 * size, center[1] - 1.5 * size)
        return newCenter
    else:
        newCenter = (center[0] - .86 * size, center[1] + 1.5 * size)
        return newCenter'''


# ------------------- Draws a hexagon in ceratain directions -----------------------
# -------- Direction is based off of the coords (tuple) of another hexagon ----------
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
    
    # ---------------------------------
    temp = hexDownRight(temp, size)
    draw_hexagon(temp,size)
    
    for i in range(0,3):
        temp = hexLeft(temp,size)
        draw_hexagon(temp,size)
    
    # ---------------------------------
    temp = hexDownLeft(temp,size)
    draw_hexagon(temp,size)
    
    for i in range(0,4):
        temp = hexRight(temp,size)
        draw_hexagon(temp,size)
        
    # ---------------------------------
    temp = hexDownLeft(temp, size)
    draw_hexagon(temp,size)
    
    for i in range(0,3):
        temp = hexLeft(temp,size)
        draw_hexagon(temp,size)
     
    # ---------------------------------
    temp = hexDownRight(temp, size)
    draw_hexagon(temp,size)
    
    for i in range(0,2):
        temp = hexRight(temp,size)
        draw_hexagon(temp,size)
    
    
    
    
#class Board():
    #def __init__self(self):
        #self.rect = self.


#pygame.draw.rect(window, (0, 0, 255), 
                 #[100, 100, 400, 100], 2)
        


# Attemp to setup entire board
boardSetup(center, size)

#Game loop begins
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            #sys.exit()
        # Allows user to hit ESCAPE to exit the game window
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
                


    # Hexagon stuff
    '''center1 = (300,300)
    
    right = hexRight(center1,size)
    left = hexLeft(center1, size)
    upLeft = hexUpLeft(center1,size)
    upRight = hexUpRight(center1,size)
    downLeft = hexDownLeft(center1,size)
    downRight = hexDownRight(center1,size)
    #center4 = multi_hex_coords(center1,size,2)
    #points = hexagon_points(center,50)
    

    # Draing hexagons
    draw_hexagon(center1,size)
    draw_hexagon(left,size)
    '''
    
    '''draw_hexagon(upLeft,size)
    draw_hexagon(upRight,size)
    draw_hexagon(downLeft,size)
    draw_hexagon(downRight,size)'''
    
    
    #pygame.draw.polygon(window, (0,0,255), points, 2)
    

    
    #points = hexagon_points(center,100)

    # Update the display
    pygame.display.flip()
    
pygame.quit()
sys.exit()