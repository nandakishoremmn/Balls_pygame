from pygame import *
from balls import *
from target import *
from player import *

done = False

def collision():
    global n
    if (player.x-player.width/2 < target.x < player.x+player.width/2) and (player.y-player.height/2 < target.y < player.y+player.height/2):
        balls.append(BALL())
        n+=1
        target.new()

def collide(ball):
    global done
    if (player.x-player.width/2 < ball.x < player.x+player.width/2) and (player.y-player.height/2 < ball.y < player.y+player.height/2):
        done = True 

init()            # Start Pygame

balls = [BALL() for i in range(n)]
target = TARGET()
player = PLAYER()
target.new()
display.set_caption('Ball game')    # And set its title

while done == False:
    screen.fill(200)    # Fill the screen with black (colour 0)
    for ball in balls:
        ball.draw()    # Draw ball
    target.draw()
    player.draw()
    display.update()

    time.delay(10)        # Slow it down!

    player.move()
    for ball in balls:
        ball.bounce()
        collide(ball)
        ball.move()
    
    collision()
    
    for e in event.get():    # Check for ESC pressed
        if e.type == KEYDOWN:
            done = True
