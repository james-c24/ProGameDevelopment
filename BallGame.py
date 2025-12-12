import pgzrun
from random import randint

TITLE = "Floppy Ball"
WIDTH = 500
HEIGHT = 500
GRAVITY = 200

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

game_over = False

class Ball:
    def __init__(self,init_x,init_y):
        self.init_x = init_x
        self.init_y = init_y
        self.vx = 200
        self.vy = 0
        self.r = 40
    def draw(self):
        pos = (self.init_x,self.init_y)
        screen.draw.filled_circle(pos,self.r,BLUE)

ball = Ball(50,100)

def draw():
    screen.clear()
    if game_over:
        screen.draw.text("Game Over.",center=(250,250),fontsize=60,color=RED)
    else:
        ball.draw()

def update(dt):
    global game_over
    if game_over:
        return
    uy = ball.vy
    ball.vy += GRAVITY * dt
    ball.init_y += (uy+ball.vy)*0.5*dt

    if ball.init_y > HEIGHT - ball.r:
        game_over = True
        return
    
    if ball.init_y > HEIGHT - ball.r:
        ball.init_y = HEIGHT - ball.r
        ball.vy = -ball.vy * 0.9

    ball.init_x = ball.init_x + ball.vx * dt

    if ball.init_x > WIDTH - ball.r or ball.init_x < ball.r:
        ball.vx = -ball.vx

def on_key_down(key):
    if key == keys.SPACE:
        ball.vy =- 10

pgzrun.go()
