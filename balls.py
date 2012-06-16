'''
Created on 30-May-2012

@author: NANDU
'''
from initialise import screen
from pygame import image
from math import ceil
from random import random, randrange


class BALL:
    
    def __init__(self,x=0,y=0):
        self.pic = image.load('images/ball.png')
        self.width = self.pic.get_width()
        self.height = self.pic.get_height()
        self.x = self.width  + randrange( 0,ceil((screen.get_width()  - x)    - 2*self.width ) )
        self.y = self.height + randrange( 0,ceil((screen.get_height() - y)*.9 - 2*self.height) )
        self.dx = (random()*2)
        self.dy = (random()*2)
          
    def move(self):
        self.x+=self.dx
        self.y+=self.dy    
        
    def reverse(self):
        self.dx = -self.dx
        self.dy = -self.dy
        
    def bounce(self):
        if self.width/2 > self.x:
            self.x = self.width/2
            self.dx = -self.dx
        if screen.get_width()-self.width/2 < self.x:
            self.x = screen.get_width()-self.width/2
            self.dx = -self.dx
        if self.height/2 > self.y:
            self.y = self.height/2
            self.dy = -self.dy
        if screen.get_height()*.9-self.height/2 < self.y:
            self.y = screen.get_height()*.9-self.height/2
            self.dy = -self.dy
            
    def draw(self):
        screen.blit(self.pic, (self.x-self.width/2, self.y-self.height/2))
            