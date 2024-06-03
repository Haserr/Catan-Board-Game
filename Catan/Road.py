# External Road class
import pygame

#Some colors
WHITE = (255,255,255) #white

# Class for house object in game
class Road():
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