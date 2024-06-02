# External gameTile class
import math
import pygame
import random


# Tile Colors
brickColor = (150,75,0)
hayColor = (236,204,162)
stoneColor = (128,128,128)
sheepColor = (144,238,144)
woodColor = (1,50,32)
blackColor = (0,0,0)

# Creates a list to store all of the tile colors
tileColorList = [brickColor,hayColor,stoneColor,sheepColor,woodColor]

# Made the mistake of making the whole board an object
# This class makes each hexagon tile an object            
class gameTile():
    def __init__(self, center, size, id):
        self.center = center
        self.size = size
        self.points = []

        # How we identify the hexagon we collided with?
        self.id = id
        
    # Function to calculate hexagon points
    def hexagon_points(self):
        points = []
        for i in range(6):
            angle_deg = 60 * i - 30
            angle_rad = math.radians(angle_deg)
            x = self.center[0] + self.size * math.cos(angle_rad)
            y = self.center[1] + self.size * math.sin(angle_rad)
            points.append((x, y))
            
        # Set here for collision
        self.points = points
        return points

    # Function to draw a hexagon
    def draw_hexagon(self, window):
        points = self.hexagon_points()
        
        # Draws a black hexagon to act as a black border
        pygame.draw.polygon(window, blackColor, points,3)
        
        # Draws the filled in hexagon
        pygame.draw.polygon(window, random.choice(tileColorList), points)