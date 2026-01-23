import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH,HEIGHT = 900,500
WIN = pygame.display.set_mode(WIDTH,HEIGHT)
pygame.display.setcaption("Space Invaders")

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

BORDER = pygame.Rect(WIDTH//2,0,10,HEIGHT)

BULLET_HIT_SOUND = pygame.mixer.Sound("hit.mp3")
BULLET_FIRE_SOUND = pygame.mixer.Sound("shoot.mp3")

HEALTH_FONT = pygame.font.SysFont('comicsans',40)
WINNER_FONT = pygame.font.SysFont('comicsans',100)

FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 55,40

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT),90))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT),270))

SPACE = pygame.transform.scale(pygame.image.load(os.path.join("space.png")),(WIDTH,HEIGHT))

def draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health):
    WIN.blit(SPACE,(0,0))
    pygame.draw.rect(WIN,BLACK,BORDER)

    red_health_text = HEALTH_FONT.render("Health: "+str(red_health),1,WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: "+str(yellow_health),1,WHITE)

    WIN.blit(red_health_text,(WIDTH-red_health_text.get_width()-10,10))
    WIN.blit(yellow_health_text,(10,10))

    WIN.blit(RED_SPACESHIP,(red.x,red.y))
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    
    for bullet in red_bullets:
        pygame.draw.rect(WIN,RED,bullet)
    
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,YELLOW,bullet)

    pygame.display.update()

def yellow_handle_movement(keys_pressed,yellow):
    if keys_pressed(pygame.K_w) and yellow.y-VEL>0:
        yellow.y -= VEL
    if keys_pressed(pygame.K_a) and yellow.x>0:
        yellow.x -= VEL
    if keys_pressed(pygame.K_s) and yellow.y+yellow.height+VEL<HEIGHT:
        yellow.y += VEL
    if keys_pressed(pygame.K_d) and yellow.x+yellow.width+VEL<WIDTH//2:
        yellow.x += VEL

def red_handle_movement(keys_pressed,red):
    if keys_pressed(pygame.K_w) and red.y-VEL>0:
        red.y -= VEL
    if keys_pressed(pygame.K_a) and red.x-red.width-VEL>WIDTH//2:
        red.x -= VEL
    if keys_pressed(pygame.K_s) and red.y+red.height+VEL<HEIGHT:
        red.y += VEL
    if keys_pressed(pygame.K_d) and red.x<WIDTH:
        red.x += VEL
