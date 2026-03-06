import pygame
from pygame.locals import *
import random
import time

def change_background(img):
    background = pygame.image.load(img)
    bg = pygame.transform.scale(background,(screen_width,screen_height))
    screen.blit(bg,(0,0))

screen_width = 500
screen_height = 500
WIN = pygame.display.set_mode((screen_width,screen_height))

score = 0
pygame.display.set_caption("Recycle Marathon")

bin_image = pygame.image.load(("bin.png"))
bin = pygame.transform.scale(bin_image,(30,50))

def bin_handle_movement(keys_pressed,bin):
    if keys_pressed[pygame.K_UP] and bin.y - 5 > 0:
        bin.y -= 5
    if keys_pressed[pygame.K_LEFT] and bin.x - 5 > 0:
        bin.x -= 5
    if keys_pressed[pygame.K_DOWN] and bin.y + 5 > 0:
        bin.y += 5
    if keys_pressed[pygame.K_RIGHT] and bin.x + 5 > 0:
        bin.x += 5
