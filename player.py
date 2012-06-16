'''
Created on 30-May-2012

@author: NANDU
'''
from initialise import screen
from pygame import image, mouse, mixer
from math import sqrt

class PLAYER:
    
    def __init__(self):
        self.x = 100
        self.y = 100
        self.pic = image.load('images/player.png')
        self.width = self.pic.get_width()
        self.height = self.pic.get_height()
        self.sound = mixer.Sound('sounds/end.wav')
    
    def play_sound(self):

        channel = self.sound.play()

        if channel is not None:
            # Get the left and right volumes
            left = float(self.x)/screen.get_width()
            right = 1.0 - left
            right, left = left/sqrt(right**2+left**2), right/sqrt(right**2+left**2)
            channel.set_volume(left, right)  
         
    def move(self):
        self.x,self.y = mouse.get_pos()    
                              
    def draw(self):
        screen.blit(self.pic, (self.x-self.width/2, self.y-self.height/2))