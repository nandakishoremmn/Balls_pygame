'''
Created on 30-May-2012

@author: NANDU
'''

from pygame import image, mixer
from initialise import screen
from math import floor, sqrt
from random import random

class TARGET:
    
    def __init__(self):
        self.size = 64
        self.x = 100
        self.y = 100
        self.pic = image.load('images/target.png')
        self.width = self.pic.get_width()
        self.height = self.pic.get_height()
        self.sound = mixer.Sound('target.wav')
    
    def play_sound(self):

        channel = self.sound.play()

        if channel is not None:
            # Get the left and right volumes
            left = float(self.x)/screen.get_width()
            right = 1.0 - left
            right, left = left/sqrt(right**2+left**2), right/sqrt(right**2+left**2)
            channel.set_volume(left, right)
        
    def new(self):
        self.x = self.width  + floor( random()*(screen.get_width()  - 2*self.width ) )
        self.y = self.height + floor( random()*(screen.get_height()*.9 - 2*self.height) )                       
        
    def draw(self):
        screen.blit(self.pic, (self.x-self.width/2, self.y-self.height/2))