'''
Created on 31-May-2012

@author: NANDU
'''
from pygame import display, init, time, event, draw, key, font
from pygame.constants import *
from balls import BALL
from target import TARGET
from player import PLAYER
from initialise import screen

color_black = 0,0,0
color_white = 255,255,255

class Game:
    def __init__(self):
        init()
        self.n = 0
        self.score = 0
        self.score_max = 10.0
        self.high = 0
        self.balls = []
        self.player = PLAYER()
        self.target = TARGET()
        self.target.new()
        display.set_caption('Ball Game')
        self.clock = time.Clock()
        self.Font = font.SysFont("arial", 40);
    
    def put_message(self):
        message = "Balls : %2d    Score : %3d    High : %3d"%(self.n,self.score,self.high)
        text = self.Font.render(message, True, (0, 0, 255))    
        screen.blit(text, (screen.get_width()/2 - text.get_width()/2,int(.9*screen.get_height())))
        display.update([[0,int(screen.get_height()*.9)],[int(screen.get_width()),int(screen.get_height()*.1)]])
        
    def check(self):
        # checks if player hits target
        if (abs(self.target.x-self.player.x) < self.target.width/2+self.player.width/2) and (abs(self.target.y-self.player.y) < self.target.width/2+self.player.height/2):
            self.balls.append(BALL(self.player.x,self.player.y))
            self.n+=1
            self.target.play_sound()
            self.target.new()
            self.score += int(max(self.score_max,5))
            self.high = max(self.high,self.score)
            self.score_max = 10.0
            self.put_message()
            self.draw()
        # checks if plater hits a ball
        for ball in self.balls:
            if (self.player.x-self.player.width/2 < ball.x < self.player.x+self.player.width/2) and (self.player.y-self.player.height/2 < ball.y < self.player.y+self.player.height/2):
                self.player.play_sound()
                self.score = 0
                self.score_max = 10.0
                self.stop = True      
                
    def update(self):
        self.player.move()
        for ball in self.balls:
            ball.bounce()
            ball.move() 
            
    def draw(self):
        screen.fill(color_black)
        draw.rect(screen, color_white, [[0,0],[int(screen.get_width()),int(screen.get_height()*.9)]])
        self.target.draw()
        self.player.draw()
        for ball in self.balls:
            ball.draw()
        display.update([[0,0],[int(screen.get_width()),int(screen.get_height()*.9)]])
        
    
    def reset(self):
        self.n = 0
        self.balls = []
        self.player = PLAYER()
    
    def handle_events(self):
        keys = key.get_pressed()
        if keys[K_q] or keys[K_ESCAPE]:
            self.quit = True
        if keys[K_SPACE] and self.stop:
            self.reset()
            self.stop = False
        for evt in event.get():
            if evt.type == QUIT:
                self.quit = True
            if evt.type == MOUSEBUTTONDOWN:
                for ball in self.balls:
                    ball.reverse()
        
    def run(self):
        self.quit = False
        self.stop = False
        self.put_message()
        while not self.quit:
            
            self.handle_events()
            
            if not self.stop:
                self.update()
                self.draw()
                self.check()
                self.score_max -= .04
            self.clock.tick(100)
            
if __name__=='__main__':
    game = Game()
    game.run()
