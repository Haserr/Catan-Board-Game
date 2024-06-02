import math
from re import X
import pygame
import random
import sys
from pygame.draw import polygon
from pygame.locals import *

# Importing external classes
from House import House
from gameTile import gameTile



# Initialized the game engine
pygame.init()

# Initialized some game colors
backGround = (0,171,255)  #blue

# Create a window and set resolution
window = pygame.display.set_mode((900,900))

# Fill the screen with a 'background' color
window.fill(backGround)

# Set fps to 60
FPS = pygame.time.Clock()
FPS.tick(60)

# Center decides on where the first game tile is placed
# Size is how big the game tile is
# numTiles is how many tiles the game has
center = (200,100)
size = 75
numTiles = 19

# Used for collision math
EPSILON = 1e-9


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
    
# Draws the whole board using the hex functions
def boardSetup(boardPieces):
    for i in range(0,numTiles):
        # First row     
        if i == 0:
            boardPieces.append(gameTile(center,size,i)) # First tile
            newCenter = hexRight(center,size)
        if i > 0 and i < 3:
            boardPieces.append(gameTile(newCenter,size,i))
            if i == 2:
                newCenter = hexDownRight(newCenter,size)
            else:
                newCenter = hexRight(newCenter,size)
            #print("newCenter",newCenter)
            
        # Second row    
        if i >= 3 and i < 7:
            boardPieces.append(gameTile(newCenter,size,i))
            if i == 6:
                newCenter = hexDownLeft(newCenter,size)
            else:
                newCenter = hexLeft(newCenter,size)
            
        # Third row    
        if i >= 7 and i < 12:
            boardPieces.append(gameTile(newCenter,size,i))
            if i == 11:
                newCenter = hexDownLeft(newCenter,size)
            else:
                newCenter = hexRight(newCenter,size)
            
        # Forth row    
        if i >= 12 and i < 16:
            boardPieces.append(gameTile(newCenter,size,i))
            if i == 15:
                newCenter = hexDownRight(newCenter,size)
            else:
                newCenter = hexLeft(newCenter,size)
            
        # Fifth(last) row    
        if i >= 16 and i < 19:
            boardPieces.append(gameTile(newCenter,size,i))
            newCenter = hexRight(newCenter,size)
        
    #boardPieces[0].draw_hexagon()
    #print(i)
    #print("Does nothing for now")

# Prints the whole board
def printBoard(boardPieces):
    for i in range(0,numTiles):
        boardPieces[i].draw_hexagon(window)



# ---- Will make the game objects classes soon ----

# Class for road object in game
#class Road():
        
# Class for city object in game        
#class City():
        
# Class for each player in the game        
#class Player():     


# ------------------------ Colision functions ---------------------------    

# Detects if there is a colision between a line and a line
def collideLineLine(l1_x, l1_y, l2_x, l2_y):
    
    # Normalize direction of the lines and start of the lines
    p = pygame.math.Vector2(*l1_x)
    line1Vec = pygame.math.Vector2(*l1_y) - p
    r  = line1Vec.normalize()
    
    q = pygame.math.Vector2(*l2_x)
    line2Vec = pygame.math.Vector2(*l2_y) - q
    s  = line2Vec.normalize()
    
    # Normal vectors to the lines
    rNV = pygame.math.Vector2(r[1], -r[0])
    sNV = pygame.math.Vector2(s[1], -s[0])
    rdotSVN = r.dot(sNV)
    
    if abs(rdotSVN) < EPSILON:
    #if rdotSVN == 0:
        #print("Parallel or very close to parellel lines") 
        return False
    
    # Distance to intersection point
    qp = q - p
    #print(qp)
    t = qp.dot(sNV) / rdotSVN
    u = qp.dot(rNV) / rdotSVN
    
    return t > 0 and u > 0 and t*t < line1Vec.magnitude_squared() and u*u < line2Vec.magnitude_squared()
    #return 0 <= t <= 1 and 0 <= u <= 1 and t * t <= line1Vec.magnitude_squared() and u * u <= line2Vec.magnitude_squared()

# Detects if there is a colision between a rectangle and a line segment
def collideRectLine(rect, p1, p2):
    return (collideLineLine(p1, p2, rect.topLeft, rect.bottomLeft) or
            collideLineLine(p1, p2, rect.bottomLeft, rect.bottomRight) or
            collideLineLine(p1, p2, rect.bottomRight, rect.topRight) or
            collideLineLine(p1, p2, rect.topRight, rect.topLeft))

# Detects if a polygon and a rectangel are intersection
# Achieved by testing each line segment in a polygone against the rectangle
def collideRectPoly(rect, poly):
    
    for i in range(len(poly) - 1):
         if collideRectLine(rect, poly[i], poly[i+1]):
            #print(" --------- Collision!!! ------------")
            return True
         # Added this since line segment of the hexagon never gets checked 
         if collideRectLine(rect, poly[5], poly[0]):
            #print(" --------- Collision!!! ------------")
            return True
    #print("No collision") 
    return False  
      


# ---------------------------------------------------------------------------------
# --------------------------------- Start of Main ---------------------------------
# ---------------------------------------------------------------------------------


# Attempt to setup board using the gameTiles Class
boardPieces = []

# Creates the whole board, appends all of the tiles to boardPieces[]
boardSetup(boardPieces)

# Prints the board to the screen
printBoard(boardPieces)

# Initiates the list of houses
houses = []

# ------------------------------ Game loop begins ------------------------------------
i = 0 #House id or index, need to change name 
mb = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mb = True
            
        # Allows user to hit ESCAPE to exit the game window
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
    # Placeing a house by getting mouse position and leftclicking
    if mb == True:            
        houses.append(House(100,100,25,25, i))
        houses[i].setXY(pygame.mouse.get_pos())
        houses[i].draw(window)
        #print(houses[i].topLeft, i)
        
        # Attempt to test collision, need to loop through all of the gameTiles
        for j in range(0,numTiles):
            if collideRectPoly(houses[i],boardPieces[j].points):
                print("Collision with hexagon:",boardPieces[j].id)
          
        
        # Id for the houses
        i = i+1
        
        # Setting mouseButton to false so only 1 house prints
        mb = False
     
    
    # Update the display
    pygame.display.flip()
    
pygame.quit()
sys.exit()