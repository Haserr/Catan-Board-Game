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

houseStartCoord = (100,100)
houseSize = (25,25)

EPSILON = 1e-9

class Board():
    def __init__(self, center, size):
        self.center = center
        self.size = size
        self.points = []
        

    # Function to calculate hexagon points
    def hexagon_points(self,center, size):
        points = []
        for i in range(6):
            angle_deg = 60 * i - 30
            angle_rad = math.radians(angle_deg)
            x = center[0] + size * math.cos(angle_rad)
            y = center[1] + size * math.sin(angle_rad)
            points.append((x, y))
            
        # Set here for collision
        self.points = points
        return points

    # Function to draw a hexagon
    def draw_hexagon(self,center, size):
        points = self.hexagon_points(center, size)
        
        # Draws a black hexagon to act as a black border
        pygame.draw.polygon(window, blackColor, points,3)
        
        # Draws the filled in hexagon
        pygame.draw.polygon(window, random.choice(tileColorList), points)
   


    # ------------------- Draws a hexagon in ceratain directions -----------------------
    # Direction is based off of the center, which are passed in as coords (tuple) of another hexagon 
    def hexUpLeft(self,center,size):
        newCenter = (center[0] - .86 * size, center[1] - 1.5 * size)
        return newCenter

    def hexUpRight(self,center,size):
        newCenter = (center[0] + .86 * size, center[1] - 1.5 * size)
        return newCenter

    def hexDownLeft(self,center,size):
        newCenter = (center[0] - .86 * size, center[1] + 1.5 * size)
        return newCenter

    def hexDownRight(self,center,size):
        newCenter = (center[0] + .86 * size, center[1] + 1.5 * size)
        return newCenter

    def hexRight(self,center,size):
        newCenter = (center[0] + 1.73 * size, center[1])
        return newCenter

    def hexLeft(self,center,size):
        newCenter = (center[0] - 1.73 * size, center[1])
        return newCenter  
    
    # Draws the whole board using the hex functions
    def boardSetup(self,center, size):
    
        # ---- Start of Drawing ----
        self.draw_hexagon(center,size)
        temp = center
    
        for i in range(0,2):
            temp = self.hexRight(temp,size)
            self.draw_hexagon(temp,size)
    
        # ------------ Top 3 Hexagons 
        temp = self.hexDownRight(temp, size)
        self.draw_hexagon(temp,size)
    
        for i in range(0,3):
            temp = self.hexLeft(temp,size)
            self.draw_hexagon(temp,size)
    
        # ------------- 2nd Row of Hexagons 
        temp = self.hexDownLeft(temp,size)
        self.draw_hexagon(temp,size)
    
        for i in range(0,4):
            temp = self.hexRight(temp,size)
            self.draw_hexagon(temp,size)
        
        # -------------- 3rd Row of Hexagons
        temp = self.hexDownLeft(temp, size)
        self.draw_hexagon(temp,size)
    
        for i in range(0,3):
            temp = self.hexLeft(temp,size)
            self.draw_hexagon(temp,size)
     
        # -------------- Last Row of Hexagons 
        temp = self.hexDownRight(temp, size)
        self.draw_hexagon(temp,size)
    
        for i in range(0,2):
            temp = self.hexRight(temp,size)
            self.draw_hexagon(temp,size)
    
# ------------------------ Attempting to make colision functions ---------------------------    

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
        print("Parallel or very close to parellel lines") 
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
    #print(poly[0], poly[1])
    #print(poly[1], poly[2])
    #print(poly[2], poly[3])
    #print(poly[3], poly[4])
    #print(poly[4], poly[5])
    #print(poly[5], poly[0])
    #print(rect) 
    for i in range(len(poly) - 1):
         if collideRectLine(rect, poly[i], poly[i+1]):
            print(" --------- Collision!!! ------------")
            return True
         # Added this since line segment of the hexagon never gets checked 
         if collideRectLine(rect, poly[5], poly[0]):
            print(" --------- Collision!!! ------------")
            return True
    return False

    


# ---- Will make the game objects classes soon ----
        

        
#class Road():
class House():
    def __init__(self,x,y,w,h,id):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h
        
        self.w = w
        self.h = h

        # References used for collision detection
        self.topLeft = [x,y]
        self.topRight = [x+w,y]
        self.bottomLeft = [x,y+h]
        self.bottomRight = [x+w,y+h]
        
        self.fillColor = WHITE
        self.stained = False
        self.id = id
        
    # Setting the new position of a rectangle to mouse position
    def setXY(self,xy):
        # The following 2 lines update the rectangle coords 
        # Now it will be placed 0.5 * width and 0.5 * height 
        # This centers the house on the mouse, so where ever you click is more accurate
        
        # Sets position of x1 and y1 and shifts rectangle to middle of mouse
        self.x1 = xy[0] - (0.5*self.w)
        self.y1 = xy[1] - (0.5*self.h)
        
        
        # Sets x2 and y2 based off of the shifted position
        self.x2 = self.x1 + self.w
        self.y2 = self.y1 + self.h
        
        # Sets references for collision detection, not used for drawing
        self.topLeft = [self.x1,self.y1]
        self.topRight = [self.x1+self.w,self.y1]
        self.bottomLeft = [self.x1,self.y1+self.h]
        self.bottomRight = [self.x1+self.w,self.y1+self.h]
        
    # Returns a coordinate
    def getXY(self):
        return(self.x1,self.y1)
    
    # Returns values needed to build a rectangle in the form of a tuple
    def rect(self):
        
        coords = self.getXY()
        
        x1 = coords[0] 
        y1 = coords[1]
        
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
board = Board(center,size) 
houses = []
#board.boardSetup(center,size)
#boardSetup(center, size)

# Attempt to setup a single house
#house = House(150,150,25,25,0)
#house.draw(window)

# House is created, now colision test
board.draw_hexagon(center,size)
#collideRectPoly(house,board.points)

print(collideLineLine((0, 0), (1, 1), (0, 1), (1, 0)))  # Expected: True (they intersect)
print(collideLineLine((0, 0), (1, 0), (0, 1), (1, 1)))  # Expected: False (they do not intersect)
# ------------------------------ Game loop begins ------------------------------------
i = 0
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
        houses.append(House(100,100, 25,25, i))
        houses[i].setXY(pygame.mouse.get_pos())
        houses[i].draw(window)
        print(houses[i].topLeft, i)
        
        # Attempt to test collision, works 50% of the time: broken
        collideRectPoly(houses[i],board.points)
        
        # Id for the houses
        i = i+1
        
        # Setting mouseButton to false so only 1 house prints
        mb = False
     
    
    # Update the display
    pygame.display.flip()
    
pygame.quit()
sys.exit()